'''
    1.excel，数据库
    python操作excel表和数据库
    1.python操作excel

    1.xlrd模块
        cmd  -->  python -m pip  install xlrd==0.9.3
    2.导入xlrd
    3.打开工作簿
    4.选择选项卡
    5.通过坐标来确定表格，并获取数据
任务1：
    大数据统计和分析：
'''
import xlrd

#开发工作簿
wb = xlrd.open_workbook(filename=r"F:\day07【excel表读写】\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

# 选项卡
# st = wb.sheet_by_name("员工管理")

all_sheet = wb.sheets()#Book(工作簿)对象方法

#全年的销售总额
#遍历返回的Sheet对象的list
xs_sum = 0
sheet_xs_sum = 0
for each_sheet in all_sheet:
    # print(each_sheet)
    sheet_xs_sum = 0
    rows = each_sheet.nrows
    cols = each_sheet.ncols
    for i in range(1,rows):
        data = each_sheet.row_values(i)
        sheet_xs_sum += data[2]*data[4]
    print(each_sheet.name,"   销售总额：",sheet_xs_sum)#sheet对象方法
    xs_sum += sheet_xs_sum
print("全年销售总额：",xs_sum)

#每件衣服的销售占比
# dict1 = ()
# for each_sheet in all_sheet:
#     for
def SaleMoneyAYear():
    # =======================================
    # 年销售额
    sum1 = 0
    sum2 = 0
    for i in range(12):
        ts = wb.sheet_by_index(i)
        for j in range(1, ts.nrows):
            getTR = ts.row_values(j)
            money1 = getTR[2] * getTR[4]
            sum1 += money1
        sum2 += sum1
    print("年销售额：{:.2f}".format(sum2))
#=======================================
# 最畅销的衣服
def MostPopularClothes():
    clothesShow = {}
    for i in range(12):
        csn = wb.sheet_by_index(i)
        for j in range(1, csn.nrows):
            getCR = csn.row_values(j)
            if getCR[1] not in clothesShow:
                clothesShow.update({getCR[1]: int(getCR[4])})
            elif getCR[1] in clothesShow:
                clothesShow[getCR[1]] += int(getCR[4])
    compareNum = 0
    MemStr = ''
    for j in clothesShow:
        if clothesShow[j] > compareNum:
            compareNum = clothesShow[j]
            MemStr = j
        else:
            pass
    print("最畅销的衣服是：", MemStr, "，共售出", int(compareNum), "件")

    # 最不畅销的衣服（全年）
    def MostNotPopularClothes():
        clothesShow = {}
        for i in range(12):
            csn = wb.sheet_by_index(i)
            for j in range(1, csn.nrows):
                getCR = csn.row_values(j)
                if getCR[1] not in clothesShow:
                    clothesShow.update({getCR[1]: int(getCR[4])})
                elif getCR[1] in clothesShow:
                    clothesShow[getCR[1]] += int(getCR[4])
        compareNum2 = 9999
        MemStr = ''
        for j in clothesShow:
            if clothesShow[j] < compareNum2:
                compareNum2 = clothesShow[j]
                MemStr = j
            else:
                pass
        print("最不畅销的（全年销售最低的）衣服是：", MemStr, "，共售出", int(compareNum2), "件")











