# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 11:28
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : requset_test.py
# @Software : PyCharm
import requests
import pprint
url = 'https://www.wangduoyun.com/index.php?r=source/dataMany&app_id=15157784&limit=200&sort=__id.desc&page=2&_=1606449036710'

querystring = {
    "r": "source/dataMany",
    "app_id": "15157784",
    "limit": "200",
    "sort": "__id.desc",
    "page": "37",
    "_": "1606449036709"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=7j35f0534ba47blvc2vs1rq731; utm_source=natural; WHISPER_UID=whisper_5fc06edd0d7347.81446340; WHISPER_CUSTOMER=%7B%22uid%22%3A%22customer_5fc06edd0d787%22%2C%22name%22%3A%22%5Cu552e%5Cu524d%5Cu54a8%5Cu8be2_5fc06edd0d787%22%2C%22avatar%22%3A%22https%3A%5C%2F%5C%2Fshenjianshou-web.oss-cn-beijing.aliyuncs.com%5C%2Favatar%5C%2Fportrait.png%22%2C%22ip%22%3A%2261.185.225.102%22%7D; shenjian-key=86b6191d02708736cc30ccb6510b8a36; Hm_lvt_552960b3c750c7ccb81aec089d49d520=1606446815; page_size=200; col_width=%5B%7B%22name%22%3A%22col9%20%22%2C%22width%22%3A132.40000915527344%7D%2C%7B%22name%22%3A%22col7%20%22%2C%22width%22%3A126%7D%2C%7B%22name%22%3A%22col6%20%22%2C%22width%22%3A145%7D%5D; Hm_lpvt_552960b3c750c7ccb81aec089d49d520=1606449037"
}
payload = ""

respon = requests.get(url, data=payload, headers=headers, params=querystring)

re = respon.json()

pprint.pprint(re)
