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
class AppleCrawler(scrapy.Spider):
    name = 'guazi_chongqing'
    start_urls = ['https://www.guazi.com/cq/buy']

    # custom_settings = {'DOWNLOAD_DELAY': 2}
    #
    # 新加的代码
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,
                                 headers={
                                     'Cookie': 'uuid=c3dc641b-ec74-4a80-e7c6-70045b14a042; ganji_uuid=1065676098741256031061; sessionid=b88402c4-0877-401a-d406-f471ab241a37; lg=1; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1536594080,1537775020; close_finance_popup=2018-09-24; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A56990982313%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1537788408; antipas=5A775754o4t00l3e6301273lKm; clueSourceCode=10103000312%2300; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22c3dc641b-ec74-4a80-e7c6-70045b14a042%22%2C%22sessionid%22%3A%22b88402c4-0877-401a-d406-f471ab241a37%22%7D; cityDomain=cq; preTime=%7B%22last%22%3A1537796533%2C%22this%22%3A1536594147%2C%22pre%22%3A1536594147%7D',
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'

                                 })

    def parse(self, response):
        res = BeautifulSoup(response.body)
        print('共%s', len(res.select('.carlist a')))
        for carItem in res.select('.carlist a'):
            print(carItem.select('h2')[0].text)
