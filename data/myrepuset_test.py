# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/26 13:15
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : myrepuset_test.py
# @Software : PyCharm
import pprint
import unittest
import requests


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_add1(self):
        payment = 'YFK202011090081'
        f'''查询付款单{payment}信息'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/getList"
        params = {
            "paymentOrderSn": f"{payment}",
            "type": 1,
            "currentPage": 1,
            "pageSize": 10
        }
        # 查询付款单返回结果
        global re
        # 付款单id
        global FDid
        # 付款单金额
        global num

        respon = requests.get(url, params)

        re = respon.json()

        FDid = re["data"][0]["id"]

        num = re["data"][0]["paymentAmount"]

        pprint.pprint(re)

    def test_add2(self):
        '''匹配发票'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/matchInvoice"

        params = {
            "ids": FDid
        }
        respon = requests.post(url, params)

        re = respon.json()

        pprint.pprint(re)

    def test_add3(self):
        '''一键匹配发票'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/automaticMatching"
        params = {
            "ids": FDid
        }
        respon = requests.post(url, params)
        # 一键匹配的返回值
        global re1
        # 匹配金额
        global num1

        re1 = respon.json()

        pprint.pprint(re1)
        global receiptList
        rer = re1['data']['receiptList'][0]
        rer1 = re1['data']['receiptList'][0:2]
        rer2 = re1['data']['receiptList'][0:3]
        receiptList = []
        if num == re1['data']['receiptList'][0]['amount']:

            receiptList.append(rer)

            pprint.pprint(receiptList)

        elif num == re1['data']['receiptList'][0]['amount'] + re1['data']['receiptList'][1]['amount']:

            receiptList.append(rer1)

            pprint.pprint(receiptList)
        elif num == re1['data']['receiptList'][0]['amount'] + re1['data']['receiptList'][1]['amount'] + \
                re1['data']['receiptList'][2]['amount']:

            receiptList.append(rer2)

            pprint.pprint(receiptList)

    def test_add4(self):
        '''匹配发票保存'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/matchSave"
        params = {
            "ids": [FDid],
            "receiptList": receiptList
        }
        headers = {
            "Content-Type": "application/json"
        }

        respon = requests.post(url, json=params, headers=headers)

        re1 = respon.json()

        pprint.pprint(re1)

    def test_add5(self):
        '''财务审核'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/financialAudit"
        params = f"[{FDid}]"
        headers = {
            "Content-Type": "application/json"
        }

        respon = requests.post(url=url, data=params, headers=headers)

        re1 = respon.json()

        pprint.pprint(re1)

    def test_add6(self):
        '''三方付款'''
        url = "https://gateway.dev.vevor.net/scp-procurement-service/controller-ThirdPartyPaymentService/front/true"
        params = f"[{FDid}]"

        headers = {
            "Content-Type": "application/json"
        }

        respon = requests.put(url=url, data=params, headers=headers)

        re1 = respon.json()

        pprint.pprint(re1)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    #     filename = './payment_test.html'  # 测试报告的存放路径及文件名
    #     fp = open(filename, 'wb')  # 创测试报告html文件，此时还是个空文件
    #
    #     suite = unittest.TestSuite()  # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    #
    #     suite.addTest(TestCase('test_add1'))  # 向测试套件中添加用例，"Influence"是上面定义的类名，"test"是用例名
    #     # runner = unittest.TextTestRunner()   # 执行套件中的用例
    #     runner = TestCase.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    #     result = runner.run(suite)  # 执行测试
    #     # print(result.success_count)  # 运行成功的数目
    #     # print(result.testsRun)  # 运行测试用例的总数
    #     # print(result.failure_count)  # 运行失败的数目
    #     fp.close()  # 关闭文件流，将HTML内容写进测试报告文件
    #
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    import unittest
    import HTMLrunnerTest

    filename = r'D:\vover\reports\ipayment_test.html'  # 测试报告的存放路径及文件名
    fp = open(filename, 'wb')  # 创测试报告html文件，此时还是个空文件
    # 自动生成测试套件
    suite = unittest.defaultTestLoader.discover('./data/', pattern='*.py')

    runner = HTMLrunnerTest.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    result = runner.run(suite)  # 执行测试
    fp.close()  # 关闭文件流，将HTML内容写进测试报告文件
