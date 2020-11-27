# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 11:28
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : requset_test.py
# @Software : PyCharm
import requests
import pprint

url = 'https://www.wangduoyun.com/index.php'

querystring = {
    "r": "source/dataMany",
    "app_id": "15157784",
    "limit": "7359",
    "sort": "__id.desc",
    "page": "1",
    "_": "1606458038903"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=7j35f0534ba47blvc2vs1rq731; utm_source=natural; WHISPER_UID=whisper_5fc06edd0d7347.81446340; WHISPER_CUSTOMER=%7B%22uid%22%3A%22customer_5fc06edd0d787%22%2C%22name%22%3A%22%5Cu552e%5Cu524d%5Cu54a8%5Cu8be2_5fc06edd0d787%22%2C%22avatar%22%3A%22https%3A%5C%2F%5C%2Fshenjianshou-web.oss-cn-beijing.aliyuncs.com%5C%2Favatar%5C%2Fportrait.png%22%2C%22ip%22%3A%2261.185.225.102%22%7D; shenjian-key=86b6191d02708736cc30ccb6510b8a36; Hm_lvt_552960b3c750c7ccb81aec089d49d520=1606446815; page_size=200; col_width=%5B%7B%22name%22%3A%22col9%20%22%2C%22width%22%3A132.40000915527344%7D%2C%7B%22name%22%3A%22col7%20%22%2C%22width%22%3A126%7D%2C%7B%22name%22%3A%22col6%20%22%2C%22width%22%3A228%7D%5D; Hm_lpvt_552960b3c750c7ccb81aec089d49d520=1606457944"
}
payload = ""

respon = requests.get(url, data=payload, headers=headers, params=querystring)

re = respon.json()

for i in range(7359):
    # 商品链接  __url
    a = '商品链接:' + re['items'][i]['__url'] + '\n'
    # 品牌    brand
    b = '品牌:' + re['items'][i]['brand'] + '\n'
    # bsr   bsr
    c = 'bsr:' + re['items'][i]['bsr'] + '\n'
    # 商品分类  categories
    d = '商品分类:' + re['items'][i]['categories'] + '\n'
    # 浏览评论数 comments_count
    e = '浏览评论数:' + re['items'][i]['comments_count'] + '\n'
    # 商品名称  name
    f = '商品名称:' + re['items'][i]['name'] + '\n'
    # 评分    score
    g = '评分:' + re['items'][i]['score'] + '\n'
    # 商品价格 current_price
    k = '商品价格：' + re['items'][i]['current_price'] + '\n'

    l = f'================================第{i}条数据================================\n'
    print(f'================================第{i}条数据================================')

    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(l)
    # 商品ID
    y = '商品ID:' + a[31:41] + '\n'
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(y)
    # print(f'商品链接:{a}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(a)
    # print(f'品牌:{b}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(b)
    # print(f'bsr:{c}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(c)
    # print(f'商品分类:{d}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(d)
    # print(f'浏览评论数:{e}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(e)
    # print(f'商品名称:{f}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(f)
    # print(f'评分:{g}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(g)
    # print(f'商品价格:{k}')
    with open('./shangpin.docx', 'a', encoding='utf-8') as h:
        h.writelines(k)
# pprint.pprint(re)
