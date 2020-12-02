# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/1 9:08
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : Reptile.py
# @Software : PyCharm
import os
import os.path
import requests


def download(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    if req.status_code == 404:
        print("404错误")
    with open('./String.html', 'wb') as filename:
        filename.write(req.text.encode())
        print("下载完成")


if __name__ == '__main__':
    url = input("请输入URL: ")
    download(url)
