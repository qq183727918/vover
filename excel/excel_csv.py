# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 10:04
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : excel_csv.py
# @Software : PyCharm

pinglun = []
with open('./pinglun.csv','r')as f:
    r = f.readlines()
    pinglun.append(r)
print(pinglun)
a = pinglun[0]
list1 = []
for i in range(5787):
    b = "'" + a[i].strip('\n')+ "'" + ','
    k = list1.append(b)

# print(list1)
list2 = []
for l in range(5787):
    f = list1[l] + '\n'
    # print(f)
    list2.append(f)
# print(list2)

for id in range(5787):
    x = list2[id]
    # print(id)
    with open('nnnn.csv','a')as fl:
        fl.writelines(x)
    # print(x)
