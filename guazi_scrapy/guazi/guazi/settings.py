# -*- coding: utf-8 -*-

# Scrapy settings for guazi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guazi'

SPIDER_MODULES = ['guazi.spiders']
NEWSPIDER_MODULE = 'guazi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules


# Configure maximum concurrent requests performed by Scrapy (deROBOTSTXT_OBEY = Falsefault: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Cookie': 'uuid=c3dc641b-ec74-4a80-e7c6-70045b14a042; ganji_uuid=1065676098741256031061; clueSourceCode=%2A%2300; sessionid=b88402c4-0877-401a-d406-f471ab241a37; lg=1; cainfo=%7B%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22version%22%3A1%2C%22platform%22%3A%221%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22c3dc641b-ec74-4a80-e7c6-70045b14a042%22%2C%22sessionid%22%3A%22b88402c4-0877-401a-d406-f471ab241a37%22%2C%22display_finance_flag%22%3A%22-%22%7D; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1536594080,1537775020; close_finance_popup=2018-09-24; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A56990982313%7D; antipas=5f7757544O003X6301273cqx; cityDomain=cq; preTime=%7B%22last%22%3A1537788165%2C%22this%22%3A1536594147%2C%22pre%22%3A1536594147%7D;',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
# }
#定义IPPool
IPPOOL=[
    {"ipaddr":"218.72.66.43:18118"},
    {"ipaddr":"114.99.26.120:18118"},
    {"ipaddr":"183.159.84.219:18118"},
    {"ipaddr":"183.159.92.201:18118"},
    {"ipaddr":"183.159.88.172:18118"},
    {"ipaddr":"113.200.156.91:8118"},
    {"ipaddr":"60.177.230.5:8118"},
    {"ipaddr":"183.159.90.23:18118"},
    {"ipaddr":"115.58.131.243:8118"},
]
#定义User-Agent代理池
UAPOOL =[
    'User-Agent:Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)'
]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'guazi.middlewares.GuaziSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'guazi.middlewares.GuaziDownloaderMiddleware': 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#     'guazi.middlewares.MYIPPOOL': 125,
#     'guazi.middlewares.UserAgentMiddleware': 120,
#  }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'guazi.pipelines.GuaziPipeline': 300,
}
#分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，
# 通过pipeline，通常将这些数字定义在0-1000范围内（0-1000随意设置，数值越低，组件的优先级越高）

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
