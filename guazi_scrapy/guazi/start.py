
from scrapy import cmdline

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

