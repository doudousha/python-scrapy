import re
import time

import requests
import urllib3
from scrapy import cmdline
from selenium.webdriver import DesiredCapabilities

cmdline.execute("scrapy crawl guazi_chongqing".split())


# 1.contents[0] 和text 区别
# 如果一个标签里面还有子标签，当调用text 获取的会包含子标签内容，
# 而contents[0]不会包含子标签内容
# 2.sub 和 replace 区别
# sub 是正则表达式re 对象的方法，
# replace 不支持对象
# 3. 相对路径导入
# 最外层的guazi文件夹没有__init__.py 文件，所以在GuzZiCrawler导入guazi.guazi.items 是错误的，
# 因为pycharm 是以文件夹方式来导入的，正确的方式应该是guazi.items 导入，但是这里建议用相对方式导入依赖"..items"

#
#
# str = "最大扭矩(N*m) 23  "
# temp =re.match(r'最大扭矩\(N\*m\)\s*(.+)\s*',str)
# print(temp )
from selenium import webdriver
from urllib3._collections import HTTPHeaderDict
from urllib.parse import urlencode

# 使用copy()防止修改原代码定义dict
# cap = DesiredCapabilities.PHANTOMJS.copy()
# cap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
# driver = webdriver.PhantomJS(executable_path="./script/phantomjs.exe",desired_capabilities=cap)
# # driver.get("https://www.guazi.com/")
# driver.get("https://www.guazi.com/cq/buy")
# data = driver.get_cookies()
# mycookie =driver.execute_script('return document.cookie;')
# print(mycookie)
# print(data)
# print(driver.page_source)
# #
# # # requests.get("https://www.guazi.com/cq/buy")