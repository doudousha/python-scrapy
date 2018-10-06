import re
import time
from urllib.parse import urlencode

import scrapy
from bs4 import BeautifulSoup

# pip install ../../whl/pywin32-223.1-cp36-cp36m-win_amd64.whl
# pip install ../../whl/Twisted-18.7.0-cp36-cp36m-win_amd64.whl
# pip install beautifulsoup4
# pip install scrapy
# scrapy startpeoject xxxxx


# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# 需要将COOKIES_ENABLED 解开注释，并且设置为false
# ROBOTSTXT_OBEY = False
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from ..items import GuaziItem


class AppleCrawler(scrapy.Spider):
    name = 'guazi_chongqing'
    start_urls = ['https://www.guazi.com/cq/buy']
    cookie = "antipas=8085n76T1192364859r85425;"
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'

    # custom_settings = {'DOWNLOAD_DELAY': 2}
    #
    # 新加的代码
    def start_requests(self):
        for url in self.start_urls:
            headers = {
                'Cookie': self.cookie,
                'User-Agent': self.userAgent
            }
            yield scrapy.Request(url, headers=headers)

    def getCookie(self):
        cap = DesiredCapabilities.PHANTOMJS.copy()
        cap["phantomjs.page.settings.userAgent"] = self.userAgent
        driver = webdriver.PhantomJS(executable_path="./script/phantomjs.exe", desired_capabilities=cap)
        driver.get(self.start_urls[0])

        mycookie = driver.execute_script('return document.cookie;')
        return mycookie

    def parse(self, response):
        res = BeautifulSoup(response.body)
        domain = "https://www.guazi.com"
        headers = {
            'Cookie': self.cookie,
            'User-Agent': self.userAgent
        }
        for carItem in res.select('.carlist a')[:2]:
            print(carItem.attrs["href"])
            # print(carItem.select('h2')[0].text)
            href = domain + carItem.attrs["href"]
            yield scrapy.Request(href,
                                 self.parseDetail,
                                 headers=headers,
                                 meta={})

    def parseDetail(self, response):

        res = BeautifulSoup(response.body)
        item = GuaziItem()
        item['title'] = re.sub(r'\r\n|\s', '', res.select('.titlebox')[0].contents[0]);

        # print('title%s' % (item.title))

        owner = res.select('.people-infor .f20')[0].text
        self.commonSet(item, re.sub(r'\r\n|\s', '', owner), 'carOwner',
                       r'车主：\s*(.+)\s*')
        for liItem in res.select('.basic-eleven li'):
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'drivingDistance',
                           r'\s*(.+)表显里程\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'filingAddress',
                           r'\s*(.+)上牌地\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'lastTime',
                           r'\s*(.+)上牌时间\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'transmissionCase',
                           r'\s*(.+)变速箱\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'displacement',
                           r'\s*(.+)排量(L)\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'numberOfTransfer',
                           r'\s*(.+)登记证为准\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'carAddress',
                           r'\s*(.+)看车地址\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'yearlyInspection',
                           r'\s*(.+)年检到期\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'trongInsurances',
                           r'\s*(.+)交强险\s*')
            self.commonSet(liItem, re.sub(r'\r\n|\s', '', liItem.text), 'commercialInsurance',
                           r'\s*(.+)商业险到期\s*')

        tables = res.select('.detailcontent table')
        # 基本参数
        for trItem in tables[0].select('tr'):
            self.commonSet(item, re.sub(r'\r\n|\s', '', trItem.text), 'standard_type',
                           r'证件品牌型号此信息为机动车行驶证上的品牌型号信息，品牌型号信息以此为准\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_producer', r'生产商\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_grade', r'级别\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_motor', r'发动机\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_gearbox', r'变速箱\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_structure', r'车生结构\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_volume', r'长*宽*高\(mm\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_wheelbase', r'轴距\(mm\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_cargoVolume', r'行李箱容积\(L\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_quality', r'装备质量\(kg\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_grade', r'级别\s*(.+)\s*')

        # 发动机参数
        for trItem in tables[1].select('tr'):
            self.commonSet(item, re.sub(r'\r\n|\s', '', trItem.text), 'motor_displacement',
                           r'排量(L)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_intakeForm', r'进气形式\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_cylinder', r'气缸\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_maxPs', r'最大马力\(Ps\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_maxNm', r'最大扭矩\(N\*m\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_fuelType', r'燃料类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_fuelLabeling', r'燃油标号\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_oilSupplyMode', r'供油方式\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_emissionStandard', r'排放标准\s*(.+)\s*')

        # 底盘及制动

        # 安全配置

        # 外部配置

        # 内部配置
        print(item)
        return item

    def commonSet(self, item, text, prop, rex):
        parttenResult = re.match(rex, text)
        if (parttenResult is not None):
            item[prop] = parttenResult[1]
