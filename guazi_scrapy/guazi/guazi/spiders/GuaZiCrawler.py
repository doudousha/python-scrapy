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
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    cookie = ''
    custom_settings = {'DOWNLOAD_DELAY': 2}


    # custom_settings = {'DOWNLOAD_DELAY': 2}
    #
    # 新加的代码
    def start_requests(self):
        pageResult = self.getPageResult()
        self.cookie = pageResult['cookie']
        self.start_urls = [('{0}/o{1}'.format(self.startUrl, i)) for i in range(1, pageResult['maxPage'])]
        print('self.start_urls %s' % self.start_urls)
        for url in self.start_urls:
            headers = {
                'Cookie': self.cookie,
                'User-Agent': self.userAgent
            }
            yield scrapy.Request(url, headers=headers)

    def getPageResult(self):
        cap = DesiredCapabilities.PHANTOMJS.copy()
        cap["phantomjs.page.settings.userAgent"] = self.userAgent
        driver = webdriver.PhantomJS(executable_path="./../script/phantomjs.exe", desired_capabilities=cap)
        driver.get(self.startUrl)

        mycookie = driver.execute_script('return document.cookie;')
        res = BeautifulSoup(driver.page_source)
        print('-----------%s' % res.select('.pageLink')[0].text)

        maxPage = re.match(r'.*\.\.\.\s*(\d+)', res.select('.pageLink')[0].text)[1]
        print('maxpage - %s' % maxPage)
        return {'cookie': mycookie, 'maxPage': int(maxPage)}

    def parse(self, response):
        res = BeautifulSoup(response.body)
        domain = "https://www.guazi.com"
        headers = {
            'Cookie': self.cookie,
            'User-Agent': self.userAgent
        }
        for carItem in res.select('.carlist a'):
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
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'drivingDistance',
                           r'\s*(.+)表显里程\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'filingAddress',
                           r'\s*(.+)上牌地\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'lastTime',
                           r'\s*(.+)上牌时间\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'transmissionCase',
                           r'\s*(.+)变速箱\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'displacement',
                           r'\s*(.+)排量\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'numberOfTransfer',
                           r'\s*(.+)登记证为准\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'carAddress',
                           r'\s*(.+)看车地址\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'yearlyInspection',
                           r'\s*(.+)年检到期\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'trongInsurances',
                           r'\s*(.+)交强险\s*')
            self.commonSet(item, re.sub(r'\r\n|\s', '', liItem.text), 'commercialInsurance',
                           r'\s*(.+)商业险到期\s*')

        tables = res.select('.detailcontent table')
        # 基本参数
        for trItem in tables[0].select('tr'):
            self.commonSet(item, re.sub(r'\r\n|\s', '', trItem.text), 'standard_type',
                           r'证件品牌型号此信息为机动车行驶证上的品牌型号信息，品牌型号信息以此为准\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_producer', r'厂商\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_grade', r'级别\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_motor', r'发动机\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_gearbox', r'变速箱\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_structure', r'车身结构\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_volume', r'长\*宽\*高\(mm\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_wheelbase', r'轴距\(mm\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_cargoVolume', r'行李箱容积\(L\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_quality', r'整备质量\(kg\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'standard_grade', r'级别\s*(.+)\s*')

        # 发动机参数
        for trItem in tables[1].select('tr'):
            self.commonSet(item, re.sub(r'\r\n|\s', '', trItem.text), 'motor_displacement',
                           r'排量\(L\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_intakeForm', r'进气形式\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_cylinder', r'气缸\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_maxPs', r'最大马力\(Ps\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_maxNm', r'最大扭矩\(N\*m\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_fuelType', r'燃料类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_fuelLabeling', r'燃油标号\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_oilSupplyMode', r'供油方式\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'motor_emissionStandard', r'排放标准\s*(.+)\s*')

        # 底盘及制动

        for trItem in tables[2].select('tr'):
            self.commonSet(item, trItem.text, 'chassis_drivingMode', r'驱动方式\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_typeOfSupport', r'助力类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_frontSuspension', r'前悬挂类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_rearSuspension', r'后悬挂类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_frontBrake', r'前制动类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_rearBrake', r'后制动类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_parkingBrakeType', r'驻车制动类型\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_frontTireSpecification', r'前轮胎规格\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'chassis_rearTireSpecification', r'后轮胎规格\s*(.+)\s*')

        ####################  安全配置   ###################

        for trItem in tables[3].select('tr'):
            self.commonSet(item, trItem.text, 'security_principalAndAssistant', r'主副驾驶安全气囊\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_roundSide', r'前后排侧气囊\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_roundHead', r'前后排头部气囊\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_tirePressureDetection', r'胎压检测\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_internalControlLock', r'车内中控锁\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_childSeat', r'儿童座椅接口\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_keylessStartUp', r'无钥匙启动\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_antiLockBrakingSystem', r'防抱死系统\(ABS\)\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'security_vehicleStabilityControlSystem', r'车身稳定控制\(ESP\)\s*(.+)\s*')

        ####### 外部配置 ##########
        for trItem in tables[4].select('tr'):
            self.commonSet(item, trItem.text, 'outer_electricSkylight', r'电动天窗\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_panoramicSunroof', r'全景天窗\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_electricallyOperatedSuctionDoor', r'电动吸合门\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_speechTrunk', r'感应后备箱\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_inductionWiper', r'感应雨刷\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_rearWiper', r'后雨刷\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_frontAndRearPowerWindows', r'前后电动车窗\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_electricAdjustmentOfRearviewMirror', r'后视镜电动调节\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'outer_rearviewMirrorHeating', r'后视镜加热\s*(.+)\s*')

        ########## 内部配置   #######
        for trItem in tables[5].select('tr'):
            self.commonSet(item, trItem.text, 'internal_multifunctionalSteeringWheel', r'多功能方向盘\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_cruiseControl', r'定速巡航\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_airConditioner', r'空调\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_automaticAirConditioning', r'自动空调\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_gps', r'GPS导航\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_PDCParkingDistanceControl', r'倒车雷达\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_rearCameraParkingAid', r'倒车影像系统\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_leatherSeat', r'真皮座椅\s*(.+)\s*')
            self.commonSet(item, trItem.text, 'internal_frontAndRearSeatHeating', r'前后排座椅加热\s*(.+)\s*')

        print(item)
        return item

    def commonSet(self, item, text, prop, rex):
        parttenResult = re.match(rex, text)
        if (parttenResult is not None):
            item[prop] = parttenResult[1]
