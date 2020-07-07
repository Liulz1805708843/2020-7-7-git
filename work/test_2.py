
# # 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, "*", i, "=", j * i, end="\t")
#     print()
#
# # 冒泡排序
# ll = [2, 5, 97, 10, 52, 12, 54, 31, 88, 99, 31, 77]
# lenth = len(ll)
# for i in range(lenth - 1, 0, -1):    #便利列表数据
#     for j in range(i):               #便利列表下标
#         if (ll[j] > ll[j + 1]):
#             ll[j], ll[j + 1] = ll[j + 1], ll[j]
# print(ll)
#
#
#
# #封装
# class  Liuzl():
#     money = 10000000000000                #属性
#     house = 10000
#     _si_you = "地下城账号"                #私有变量
#     __feichang_siyou="火之意志"
#     def shou_yi(self):                    #实例方法
#         print("抠鼻")
#     def __init__(self,a1):
#         self.a = a1
#
# class Yupeng(Liuzl):                      #方法继承
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,*kwargs)
#     ai_hao="吃屎"
#     pass
#
# y = Yupeng(1111)
#
# print(y.ai_hao)
# print(y.money)
# print(y.house)
# y.shou_yi()
# print(y.a)


# s=[1,2,3,4,5]
# p= {9,8,7}
# print(list(p))
# print(tuple(s))
# print(set(s))
#
#
#
# f = open("aaa.txt","w")
# f.write("hello 沙雕余鹏")
# f.close()



# f = open("aaa.txt","w")
# # f.write("hello 沙雕余鹏")
# f.writelines(["沙雕余鹏\n","憨批余鹏\n","憨批余鹏"])
# # print(f.writable());
# f.close()

# f = open("aaa.txt","r")
# # print(f.readline())
# print(f.readlines())
# f.close()

# a="1,2,3,4,5,6,7,8,9"
# print(a[0:3])
# print(a[::-1])


# a1="   沙雕余鹏，憨批余鹏，傻逼余鹏  "       #去空格
# print(a1.strip())



# a="沙雕，憨批，傻逼"           #
# print(a.split(","))
#
#
# with open("aaa.txt","r") as f:
#     lines=f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""),end='')

# c = "小明,小红.张"
# c = c.replace(".", ",")
# print(c)



# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} * {} = {}".format(j,i,i*j),end="\t")
#     print()

# l = [1,5,2,85,44,65,44]
# lenth = len(l)
# for i in range(lenth - 1,0,-1):
#     for j in range(i):
#         if(l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)


# print("{:.3f}".format(2.123456789))
# print("{:>10}".format("1"))
#
#
# a = [50,21,31,64,51]
# a[0:2] = [50,50]
# print(a)


#新增数据
# a = [1,2,3,4]
# # a.append(5)
# a.extend(['444',555])
# # a.insert(0,555)
# print(a)


# #删除数据
# a = [1,2,3,4,5,6,7]
# b = [True,9,8,7,6,5]      #True为1     False为0 ----remove
# a.pop(0)
# a.remove(5)
# b.pop(1)
# print(a)
# print(b)
# b.clear()
# print(b)
# a.clear()
# print(a)


# a ={"name" : "沙雕余鹏","age":"23","sex":"人妖"}
# a["爱好"] = "吃屎"
# a.update({"addr":"厕所","学历":"小本毕业"})
# print(a)

# a = 10
# b = 0
# print(a/b)

# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         print(e)
# print(div(10,0))


class CustomException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return self.value
a= 1
try:
    if a== 0:
        print("a={} 触发异常".format(a))
        raise CustomException
    print("a={} 未触发异常".format(a))
except CustomException as e:
    print(e)