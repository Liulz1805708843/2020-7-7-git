# '''
# # 测试
# a = "沙雕"
# b = "余鹏"
# print(a + b)
# '''
# '''
# #解包赋值
# x,y,*z=(1,2,3,4,5,6)
# print(x)
# print(y)
# print(z)
# '''
#
#
# a = 20
# b = 10
# print(a >= b)
#
#
# z=123456
# z //=10
# print(z)
# print(z % 10)
#
#
#
# a = [1,2,3,4]
# if(1 in a and 2 in a):
#     print("成功")
# else:
#     print("失败")
#
#
# # score = int(input("请输入成绩:"))
# # if(score > 0 and score <60):
# #     print("不及格")
# # elif(score >=60 and score <=70):
# #     print("及格")
# # elif(score >70 and score <80):
# #     print("良好")
# # else:
# #     print("优秀")
#
#
# score = int(input("请输入成绩:"))
# if score in range(0,60):
#     print("不及格")
# elif(score >=60 and score <=70):
#     print("及格")
# elif(score >70 and score <80):
#     print("良好")
# else:
#     print("优秀")


#

# flag = True;
# a=55
# while flag:
#     b=int(input("请输入数字"))
#     if(b == a):
#         print("猜对了")
#         flag = False
#     elif (b < a) :
#         print("小了")
#     elif (b > a):
#         print("大了")


# for i in range(1,100):
#     if(i % 3 != 0):
#         continue
#     print(i)


# def shangyushu(a ,b = 20):
#     if(b == 0):
#         return None
#     else:
#         return (a // b,a%b)
#
# res = shangyushu(a=10,b=0)
#
# if res is None:
#     print("除数不能为0")
# else:
#     print("商",res[0],",余数",res[1])


# def shangyushu(a ,b = 20):
#     return a+b
# print(shangyushu(5))

#
def sum1(b, d, *args, a, c, **kwargs):  # 动态位置参数         动态关键词参数
    print(kwargs)
    print(a)
    print(c)
    print(b)
    print(d)

    s = 0;
    for i in args:
        s += i
    return s


print(sum1(5, 2, 3, 4, a=1, c=2, b='xx', names="沙雕余鹏", age=20, d="dd"))

# class cals():        #类  类--包含变量以及方法
#
#     c = None
#     def __init__(self,a1,b1):  #构造方法  魔法函数
#         self.a=a1
#         self.b=b1
#
#     def jiafa(self):
#         self.c = self.a + self.b
#     def jianfa(self):
#         self.c = self.a - self.b
#     def get_c(self):
#         print(self.c)
# ca = cals(50,60)   #对象  类的实体化
#
# ca.jiafa()
# ca.get_c()


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",i*j,end="\t")
#     print()


# for i in range(9,0,-1):
#     for j in range(9,i-1,-1):
#         print(j,"*",i,"=",i*j,end="\t")
#     print()


# l = [9,10,6,21,85,98,888,32,42,2,5,1,6]
# lenth=len(l)
# for i in range(lenth-1,0,-1):    #外层循环确定下标
#     for j in range(i):            #便利未排序好的list
#         if(l[j] > l[j+1]):         #相邻数据如果前面大于后面，则交换位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
#
#
