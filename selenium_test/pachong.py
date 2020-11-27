# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 14:39
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : pachong.py
# @Software : PyCharm
from selenium import webdriver

url = 'https://www.amazon.com/dp/B07TG72L1L?th=1&psc=1&language=en_US'
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(url)

# 商品名称
productName = driver.find_element_by_id('productTitle').text
# 商品价格
commodityPrice = driver.find_element_by_id('priceblock_ourprice').text
# 商品分类
# categories = driver.find_element_by_id('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul').text
# 浏览评论数
comment = driver.find_element_by_id('acrCustomerReviewText').text
# 评价
evaluate = driver.find_element_by_id('acrPopover').text
print(productName)
print(commodityPrice)
# print(categories)
print(comment)
print(evaluate)

driver.quit()
