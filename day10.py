#水杯
# class shuibei:
#     weight = ''
#     volume = ''
#     color = ''
#     caizhi = ''
#     def cf(self):
#         print("能存放液体")
#
# sbei = shuibei()
#
# sbei.weight = '15cm'
# sbei.volume = '300'
# sbei.color = '粉色'
# sbei.caizhi = '玻璃'
#
# sbei.cf()

#笔记本电脑
# class computer:
#     pmsize = 0
#     price = 0
#     cpu = ''
#     neicun = 0
#     djtime = 0
#     def dz(self,name):
#         print(name,"能打字")
#     def pg(self,name):
#         print(name,"能打游戏")
#     def ksp(self,name):
#         print(name,"能看视频")
#
# cp = computer()
#
# cp.dz("电脑")
# cp.pg("电脑")
# cp.ksp("电脑")

#空调
# class kongtiao:
#     _brand = ''
#     _price = 0
#
#     def setbrand(self,brand):
#         self._brand = brand
#
#     def getbrand(self):
#         return self._brand
#
#     def setprice(self,price):
#         self._price = price
#
#     def getprice(self):
#         return self._price
#
#     def kaiji(self):
#         print("空调开机了...")
#
#     def dsguanji(self,minute):
#         print("空调将在",minute,"分钟后自动关闭...")
#
#     def show(self):
#         print("空调的品牌是:",self._brand,"    空调的价格:",self._price)
#
# kt = kongtiao()
# kt.setbrand("格力")
# kt.setprice(10000)
# kt.show()
# kt.kaiji()
# kt.dsguanji(3)

#学生
# class student:
#     _name = ''
#     _age = 0
#
#     def setname(self, name):
#         self._name = name
#
#     def getname(self):
#         return self._name
#
#     def setage(self,age):
#         self._age = age
#
#     def getage(self):
#         return self._age
#
#     def introduction(self):
#         print("大家好，我叫",self._name,",今年",self._age,"岁了！")
#
#     def compare_age(self,student):
#         if self._age > student._age:
#             print("我比同桌大",(self._age - student._age),"岁！")
#         elif self._age < student._age:
#             print("我比同桌小",(student._age - self._age),"岁！")
#         else:
#             print("我和同桌一样大！")
# st = student()
# tz = student()
# st.setname("空调")
# st.setage(18)
# tz.setname("水杯")
# tz.setage(18)
#
# st.introduction()
# st.compare_age(tz)
# tz.compare_age(st)

#打电话业务逻辑
class People:
    __name = ''
    __gender = ''
    __age = 0
    __cost = 0   # 剩余话费
    __brand = ''   # 品牌
    __battery = 0  # 电池容量
    __size = 0    # 屏幕大小
    __standby = 0   # 最大待机时长
    __integral = 0  # 积分

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setAge(self, age):
        if age <= 0 or age >= 120:
            print('年龄非法！')
        else:
            self.__age = int(age)

    def getAge(self):
        return self.__age

    def setCost(self, cost):
        self.__cost = float(cost)

    def getCost(self):
        return self.__cost

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        if battery < 0:
            print('电池容量不能为负！')
        else:
            self.__battery = float(battery)

    def getBattery(self):
        return self.__battery

    def setSize(self, size):
        if size <= 0:
            print('屏幕大小输入非法！')
        else:
            self.__size = int(size)

    def getSize(self):
        return self.__size

    def setStandby(self,standby):
        self.__standby = int(standby)

    def getStandby(self):
        return self.__standby

    def setIntegral(self, integral):
        if integral < 0:
            print('积分不能为负！')
        else:
            self.__integral = int(integral)

    def getIntegral(self):
        return self.__integral

    def show(self):
        print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age,'\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand,'\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长',self.__standby, '分钟\n所拥有积分：', self.__integral)


p = People()
p.setName(input('输入姓名'))
p.setGender(input('输入性别'))
p.setAge(int(input('输入年龄')))
p.setCost(float(input('输入手机剩余话费')))
p.setBrand(input('输入手机品牌'))
p.setBattery(float(input('输入电池容量')))
p.setSize(int(input('输入手机屏幕大小')))
p.setStandby(int(input('输入手机最大待机时长')))
p.setIntegral(int(input('输入拥有积分')))
p.show()
cc = p.getCost()
dd = p.getIntegral()

while True:
    a = int(input('需要打电话还是发短信：（1或2）'))
    if a == 1:
        a_1 = input('输入短信内容：')
        print('短信内容为：\n', a_1)
    elif a == 2:
        a_1 = int(input('输入电话号码：'))
        a_2 = int(input('输入打多长时间：'))
        if a_1 == None: print('不能为空！')
        elif a_1 <= 1: print('电话费不够了！')
        else:
            print('电话已拨通！')
        if a_2 >= 0 and a_2 <= 10:
            if dd >= a_2 * 15:
                dd -= a_2 * 15
            else:
                cc -= a_2 * 1
        elif a_2 > 10 and a_2 <=20:
            if dd >= a_2 * 39:
                dd -= a_2 * 39
            else:
                cc -= a_2 * 0.8
        else:
            if dd >= a_2 * 48:
                dd -= a_2 * 48
            else:
                cc -= a_2 * 0.65

        print('剩余话费为：', cc)
        print('剩余积分为：', dd)
    else:
        break









