#华氏温度转换为摄氏温度  $C=(F-32)\div 1.8$   f:华氏度   c：摄氏度
'''
f=int(input("请输入华氏温度："))
#print(f)
c=int((f-32)/1.8)
print("摄氏温度为：",c)
'''

#输入圆的半径计算周长和面积
'''
r=float(input("请输入圆的半径："))
l=3.14*2*r
s=3.14*r*r
print("圆的周长：",l)
print("圆的面积：",s)
'''

#输入年份判断是不是闰年
'''
y=int(input("请输入年份："))
#能被4整除但不能被100整除  或者  能被400整除
if(y/4==0 and y/100!=0):
    print("是闰年")
elif(y/400==0):
    print("是闰年")
else:
    print("不是闰年")
'''

#英制单位英寸与公制单位厘米互换
#1 厘米 = 0.39英寸; 1 英寸 = 2.54厘米
'''
inch=float(input("请输入英制单位英寸："))
cm=0.39*inch
print('%f 厘米'%(cm))
'''

#百分制成绩转换为等级制成绩
'''
sorce=int(input("请输入成绩:"))
if(sorce>=90):
    print("A")
elif(sorce>=80 and sorce<90):
    print("B")
elif(sorce>=70 and sorce<80):
    print("C")
elif(sorce>=60 and sorce<70):
    print("D")
else:
    print("E")
'''

#输入三条边长，如果能构成三角形就计算周长和面积
'''
a=float(input("第一条边长:"))
b=float(input("第二条边长:"))
c=float(input("第三条边长:"))

if((a+b)>c and (b+c)>a and (a+c)>b):
    l=a+b+c
    p=l/2
    print("三角形的周长：",l)
    s=pow(p*(p-a)*(p-b)*(p-c),0.5)
    print("三角形的面积：",s)
'''