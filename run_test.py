# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/26 13:13
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : run_test.py
# @Software : PyCharm
#自动化把用例加入套件
#自动化生成测试报告
import unittest
import HTMLrunnerTest

filename = r'D:\work\c2\vover\report\payment_test.html'    #测试报告的存放路径及文件名
fp = open(filename, 'wb')    # 创测试报告html文件，此时还是个空文件
#自动生成测试套件
suite = unittest.defaultTestLoader.discover('./data/',pattern='*.py')

# suite = unittest.TestSuite()   # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
# suite.addTest(Influence('test'))  # 向测试套件中添加用例，"Influence"是上面定义的类名，"test"是用例名
# runner = unittest.TextTestRunner()   # 执行套件中的用例
runner = HTMLrunnerTest.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
result = runner.run(suite)   # 执行测试
fp.close()   # 关闭文件流，将HTML内容写进测试报告文件
