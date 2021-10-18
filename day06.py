import random

print("***************************")
print("*    中国银行账户管理系统    *")
print("***************************")
print("*          1、开户         *")
print("*          2、存钱         *")
print("*          3、取钱         *")
print("*          4、转账         *")
print("*          5、查询         *")
print("*          6、再见         *")
print("***************************")

# 开户逻辑
bank = {}  # 空的银行账户数据库
# 'Frank': {'account': 10936377, 'password': '123', 'country': '中国', 'province': '山东', 'street': '蓝翔', 'door': '001'},
bank_name = "中国银行M78分行"


# 传入参数添加到字典里面
def bank_add(account, username, password, country, province, street, door):
    if username in bank:  # 说明用户已存在
        return 2
    elif len(bank) >= 100:
        return 3
    else:
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名")
    password = input("请输入您的用户密码")
    print("下面请输入你的详细地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满请到其他银行开户")
    elif add == 2:
        print("请输入其他用户名")
    elif add == 1:
        print("开户成功,下面是你的详细信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


# 存钱
def bank_cq():
    username_cq = input("请输入用户名：")
    account_cq = input("请输入账号：")
    if username_cq in bank:
        cq_money = int(input("请输入存款的金额："))
        bank[username_cq]["money"] += cq_money
        info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            当前余额：%s
                            开户行名称：%s
               '''
        print(info % (username_cq, account_cq, bank[username_cq]["money"], bank_name))
    else:
        print("此用户不存在")


# 取钱
def bank_qq():
    username_qq = input("请输入用户名：")
    account_qq = input("请输入账号：")
    pwd_qq = input("请输入密码：")
    if username_qq in bank:
        if pwd_qq in bank:
            qq_money = int(input("请输入取款金额："))
            if qq_money <= bank[username_qq]["money"]:
                bank[username_qq]["money"] -= qq_money
                info = '''
                                            ------------个人信息------------
                                            用户名:%s
                                            账号：%s
                                            当前余额：%s
                                            开户行名称：%s
                               '''
                print(info % (username_qq, account_qq, bank[username_qq]["money"], bank_name))
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 转账
def bank_zz():
    username_zc = input("请输入转出用户名")
    account_zc = input("请输入转出账号")
    pwd = input("请输入密码：")
    username_zr=input("请输入转入用户名：")
    account_zr = input("请输入账号：")
    if (username_zr, username_zc) in bank:
        if pwd in bank[username_zc]["password"]:
            zz_money = input("请输入转账金额：")
            if zz_money <= bank[username_zc]["money"]:
                bank[username_zc]["money"] -= zz_money
                bank[username_zr]["money"] += zz_money
                info = '''
                                                            ------------个人信息------------
                                                            转出账户用户名：%s
                                                            账号：%s
                                                            当前余额：%s
                                                            开户行名称：%s
                                               '''
                print(info % (username_zc,account_zc, bank[username_zc]["money"], bank_name))
                info = '''
                                                            ------------个人信息------------
                                                            转入账号用户名：%s
                                                            账号：%s
                                                            当前余额：%s
                                                            开户行名称：%s
                                               '''
                print(info % (username_zr,account_zr, bank[account_zr]["money"], bank_name))
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 查询
def bank_chaxun():
    account = input("请输入账号：")
    pwd = input("请输入密码：")
    if account in bank:
        if pwd in bank[account]["password"]:
            info = '''
                            ------------个人信息------------
                            当前账号：%s
                            密码：%s
                            当前余额：%s
                            用户居住地址：%s%s%s%s
                            当前账户的开户行：%s
                    '''
            print(info % (account, pwd, bank[account]["money"], bank[account]["country"], bank[account]["province"],
                          bank[account]["street"], bank[account]["door"], bank_name))
        else:
            print("输入的密码错误")
    else:
        print("该用户不存在")


while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        print("1、开户")
        useradd()
        print(bank)
    elif index == 2:
        print("2、存钱")
        bank_cq()
    elif index == 3:
        print("3、取钱")
        bank_qq()
    elif index == 4:
        print("4、转账")
        bank_zz()
    elif index == 5:
        print("5、查询")
        bank_chaxun()
    elif index == 6:
        print("bye")
        break
