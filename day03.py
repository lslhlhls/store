#实现输入10个数字，并打印10个数的求和结果
'''
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(len(list1)):
    sum+=list1[i]
print(sum)
'''

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
import math

'''
list=[]
sum=0
for i in range(10):
    print('第%d个数：'%(i+1))
    list.append(int(input()))
for i in range(len(list)):
    sum+=list[i]
    avg=float(sum/len(list))
print("最大值：",max(list))
print("和：",sum)
print("平均值：",avg)
'''

#使用random模块，如何产生 50~150之间的数？
'''
import random
print(random.randint(50,150))
'''

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a=int(input("第一条边："))
b=int(input("第二条边："))
c=int(input("第三条边："))
if((a+b)>c and (b+c)>a and (a+c)>b):
    if (a==b==c):
        print("三角形为等边三角形")
    elif(a==b or a==c or b==c):
        print("三角形是等腰三角形")
    elif((a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b)):
        print("三角形为直角三角形")
    else:
        print("三角形为普通三角形")
else:
    print("不能构成三角形")
'''

#有以下两个数，使用+，-号实现两个数的调换  a=56 b=78 转换  a=78 b=56
'''
a=56
b=78
c=a+b
b=c-b
a=c-a
print("转换后a=",a)
print("转换后b=",b)
'''

#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）

# user="root"
# password="admin"
# i=1
# count=0
# for i in range(3):
#     user1=input("请输入用户名：")
#     password1=input("请输入密码：")
#     if(user1!=user or password1!=password):
#         print("输入的信息错误")
#         count=count+1
#         if count==3:
#             print("账号已锁定")
#     else:
#         print("登陆成功")
#         break



#编程实现下列图形的打印
# num = int(input('请输入行数：'))
# list1 = []
# for n in range(num):
#     row = [1]
#     list1.append(row)
#     if n == 0:
#         print(row)
#         continue
#     for m in range(1, n):
#         row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#     row.append(1)
#     print(row)

# i = 1
# n = int(input("请输入："))
# while i <= n:
#     j = 1
#     while j <= i:
#         print(f'{i}*{j}={i * j}', end=" ")
#         j += 1
#     print()
#     i += 1

# 倒叙的九九乘法表
# for i in range(9, 0, -1):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end=" ")
#     print()

# 青蛙爬井
# high = 20
# frog = 0
# day = 1
# while True:
#     frog += 3
#     if frog >= high:
#         break
#     else:
#         day += 1
#         frog -= 2
# print(day)

# 左边的都合法，右边的都不合法

# 20以内的阶乘之和

# sum = 0
# for i in range(1, 21):
#     sum += math.factorial(i)
# print(sum)





