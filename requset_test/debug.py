# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 13:06
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : debug.py
# @Software : PyCharm
data = {'items': [{
    '__flag': 0,
    '__id': 1366,
    '__latest': 1,
    '__pk': 'f22566c3c468002beb9f2104aa843290',
    '__time': '2020-11-26 23:10:17',
    # 商品链接
    '__url': 'https://www.amazon.com/dp/B07LF4YZCG?th=1&psc=1&language=en_US',
    '__version': 0,
    # 品牌
    'brand': 'Visit the Happybuy Store',
    # bsr
    'bsr': '["244,243 in Electronics","941 in Floor Cord Covers"]',
    # 商品分类
    'categories': '["Electronics","Accessories & Supplies","Cord '
                  'Management","Floor Cord Covers"]',
    # 浏览评论数
    'comments_count': '11 ratings',
    'current_price': '',
    'description': '',
    'detail': 'NaN',
    'images': '['
              '{"image_url":"https://images-na.ssl-images-amazon.com/images/I/81QkH2q3U0L._AC_SL1500_.jpg"},'
              '{"image_url":"https://images-na.ssl-images-amazon.com/images/I/71ixhhL0q0L._AC_SL1500_.jpg"},'
              '{"image_url":',
    'keyword': '',
    # 商品名称
    'name': 'Happybuy 3 Pack Driveway Rubber Curb Ramps Kit Heavy Duty '
            'Car Threshold Ramp 2.5 Inch High 1-Channel Cord Cover '
            'Curbside Bridge Ramp for Loading Dock Garage Sidewalk '
            '(1-Channel, 3Pack-Curb Ramp)',
    'params': '[]',
    'product_id': 'B07LF4YZCG',
    'rank': '',
    # 评分
    'score': '4.4',
    'sku': '[]',
    'sold_by': 'FBM',
    'stock': '',
    'url': 'https://www.amazon.com/dp/B07LF4YZCG?th=1&psc=1&language=en_US'}]}
# 商品链接  __url
a = data['items'][0]['__url']
# 商品ID
b = a[26:36]
h = '商品价格:' + data['items'][0]['current_price'] + '\n'
# # 品牌    brand
# b = data['items'][0]['brand']
# # bsr   bsr
# c = data['items'][0]['bsr']
# # 商品分类  categories
# d = data['items'][0]['categories']
# # 浏览评论数 comments_count
# e = data['items'][0]['comments_count']
# # 商品名称  name
# f = data['items'][0]['name']
# # 评分    score
# g = data['items'][0]['score']
#
print(f'商品链接:{b}')
# print(f'品牌:{b}')
# print(f'bsr:{c}')
# print(f'商品分类:{d}')
# print(f'浏览评论数:{e}')
# print(f'商品名称:{f}')
# print(f'评分:{g}')
print(f'商品价格:{h}')
