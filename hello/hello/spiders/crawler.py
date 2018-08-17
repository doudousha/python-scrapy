import scrapy
from bs4 import BeautifulSoup


class AppleCrawler(scrapy.Spider):
    name = 'hello'
    start_urls = ['http://www.cnvex.cn/']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        print(res)
        print('---------------------获取页面标题----------------------------')
        print(res.select('title')[0])
        print('---------------------获取所有文章标题标签----------------------------')
        print(res.select('.news-slide .short p'))
        print('---------------------获取图片-----------------------------')
        for newItem in res.select('.news-slide img'):
            print(newItem.attrs["src"])
        print('---------------------获取所有文章标题----------------------------')
        for newItem in res.select('.news-slide p'):
            print(newItem.text)
