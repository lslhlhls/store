import pymysql
import xlrd

#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("F:\Pyhton自动化测试\Python\day07【excel表读写】\任务\每个月的销售情况.xls",encoding_override=True)
sheet = book.sheet_by_name("1月")

#建立一个mysql连接
con = pymysql.connect(host="localhost",user="root",password="password")

cursor = con.cursor()

#创建插入SQL语句
query = "insert into mon1 (date,cname,price,fnum,dsales) values (%s,%s,%s,%s,%s)"

#创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1,sheet.nrows):
    date = sheet.cell(r,1).value
    cname = sheet.cell(r,2).value
    price = sheet.cell(r,3).value
    fnum = sheet.cell(r,4).value
    dsales = sheet.cell(r,5).value
    values = (date,cname,price,fnum,dsales)
    cursor.execute(query,values)

con.commit()
cursor.close()
con.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")

# con = pymysql.connect(host="localhost",user="root",password="password")
#
# #创建控制台
# cursor = con.cursor()
#
# sql = "create "
# param = []
#
# #执行
# cursor.execute(sql,param)
#
# #提交到数据库里
# con.commit()
#
#
# #关闭
# cursor.close()
# con.close()

# author:jason
# import random
# from select import select
# from turtle import update
#
# import pymysql
# #银行库
# bank = {}
# bank_name = "中国工商银行昌平支行"
# bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项
# # 开户成功的信息模板
# myinfo='''
#     \033[0;32;40m
#     ------------账户信息------------
#     账号：{account}
#     姓名：{username}
#     密码：{password}
#     地址：
#         国家：{country}
#         省份：{province}
#         街道：{street}
#         门牌号：{door}
#     账户余额：{money}
#     注册银行名：{bank_name}
#     -------------------------------
#     \033[0m
# '''
#
#
# # 欢迎模板
# welcome = '''
# ***********************************
# *      中国工商银行账户管理系统       *
# ***********************************
# *               选项              *
# '''
#
# welcome_item = '''*              {0}.{1}             *'''
#
# def print_welcome():
#     print(welcome,end="")
#     keys = bank_choice.keys()
#     for i in keys:
#         print(welcome_item.format(i,bank_choice[i]))
#     print("**********************************")
#
# # 输入帮助方法：chose是打印选项
# def inputHelp(chose,datatype="str"):
#     while True:
#         print("请输入",chose,":")
#         i = input(">>>:")
#         if len(i) == 0:
#             print("该项不能为空！请重新输入！")
#             continue
#         if datatype != "str":
#             return int(i)
#         else:
#             return i
#
# # 判断是否存在该银行选项
# def  isExists(chose,data):
#     if chose in data:
#         return True
#     return False
#
#
# # 获取随机码
# def  getRandom():
#     li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
#     string = ""
#     for i in range(8):
#         string =  string + li[int(random.random()* len(li))]
#     return string
#
# # 通过账号获取账户信息
# def findByAccount(account):
#     for i in bank.keys():
#         if bank[i]["account"] == account:
#             return i
#     return None
#
# # 银行的开户方法
# def bank_addUser(username,password,country,province,street,door,money):
#
#     # 查询是否已满
#     sql = "select count(*) from user"
# 	param = []
# 	data = select(sql,param)
# 	if data >= 100:
#         return 3
#
#
#     # 查询是否存在
# 	sql1 = "select * from user where username  = %s"
# 	param1 = [username]
# 	data1 = select(sql1,param1)
#
#     if len(data1) != 0:
#         return 2
#
#     # 插入数据
#     sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     param2 = [getRandom(),username,password,country,province,street,door,money,"2021-10-28",bank_name]
#     update(sql2,param2)
#     return 1
#
# # 银行的存钱方法
# def bank_saveMoney(ac,money):
#     data = findByAccount(ac)
#     if data != None and len(data) != 0:
#         sql = "update user set money=money+%s where account = %s"
#         param = [money, ac]
#         update(sql, param)
#         return True
#     return False
#
# # 银行的查询功能
# def bank_selectUser(account,password):
#
#     uname = findByAccount(account)
#
#     if uname != None and len(uname) != 0:
#         if password == bank[uname]["password"]:
#             user = bank[uname]
#             print(myinfo.format(account=user["account"],
#                             username=uname,
#                             password=user["password"],
#                             country=user["country"],
#                             province=user["province"],
#                             street=user["street"],
#                             door=user["door"],
#                             money=user["money"],
#                             bank_name=user["bank_name"]
#                             ))
#         else:
#             print("用户密码错误！")
#     else:
#         print("该用户不存在！")
#
# # 银行的取钱功能
# def bank_takeMoney(account,password,money):
#     uname = findByAccount(account)
#     if uname != None:
#         if bank[uname]["password"] == password:
#             if bank[uname]["money"] < money:
#                 return 3
#             else:
#                 bank[uname]["money"] -= money
#                 return 0
#         else:
#             return 2
#     else:
#         return 0
#
# # 转账功能
# def transformMoney():
#     output = inputHelp("转出的账号")
#     input = inputHelp("转入的账号")
#     outputpass =  inputHelp("转出的密码")
#     outputmoney = inputHelp("要转出的金额","int")
#
#     f = bank_transformMoney(output,input,outputpass,outputmoney)
#
#     if f == 1:
#         print("转出或转入的账号不存在！")
#     elif f == 2:
#         print("输入密码错误！")
#     elif f == 3:
#         print("转账金额不足！")
#     elif f == 0:
#         print("转账成功！")
#         print("您的个人信息：")
#         bank_selectUser(output,outputpass)
#     elif f == 4:
#         print("转账失败！")
#
# # 查询账户方法
# def selectUser():
#     account = inputHelp("账号")
#     password = inputHelp("密码")
#
#     bank_selectUser(account,password)
#
# # 核心程序
# while True:
#
#     print_welcome()
#     chose = inputHelp("选项")
#     if isExists(chose,bank_choice):
#         if chose  == "1":
#             addUser()
#         elif chose == "2":
#             saveMoney()
#         elif chose == "3":
#             takeMoney()
#         elif chose == "4":
#             transformMoney()
#         elif chose == "5":
#             selectUser()
#         elif chose == "6":
#             print("Bye,Bye您嘞！！！！")
#             break
#     else:
#         print("不存在改选项，别瞎弄！")