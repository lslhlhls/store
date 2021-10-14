# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔","19","女","210","Oracle",600,"60"],
#     ["许褚","45","男","230","Tencent",700 ,"10"]
# ]

#统计每个人的平均薪资
# sum=0
# for i in range(4):
#     sum=sum+names[i][5]
# avg=sum/4
# print(avg)

#统计每个人的平均年龄
# sum=0
# for i in range(4):
#     sum+=int(names[i][1])
# avg=sum/4
# print(avg)

#公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# names.insert(0,["刘备","45","男","220","alibaba",500,"30"])
# print("新列表为：",names)

#统计公司男女人数
# summ=0
# sumw=0
# for i in range(4):
#     if names[i][2]=="女":
#         sumw+=1
#     else:
#         summ+=1
# print("女生人数：",sumw)
# print("男生人数：",summ)

#每个部门的人数
# sum10=0
# sum50=0
# sum60=0
# for i in range(4):
#     if names[i][6]=="10":
#         sum10+=1
#     elif names[i][6]=="50":
#         sum50+=1
#     else:
#         sum60+=1
# print("部门编号为10的人数：",sum10)
# print("部门编号为50的人数：",sum50)
# print("部门编号为60的人数：",sum60)

#
# sorce=[
#     ["罗恩", 23,35 ,44],
#     ["哈利" ,60, 77 ,68 ,88, 90],
#     ["赫敏", 97 ,99 ,89 ,91, 95, 90],
#     ["马尔福" ,100, 85 ,90]
# ]
# sum=0
# for i in range(len(sorce)):
#     for j in range(1,len(sorce[i])):
#         sum+=int(sorce[i][j])
#     print(sum)
#     sum=0

#
# num= int(input("请输入一个数："))
# while num!=0:
#     print(num % 10)
#     num = num // 10

#请对下列列表进行冒泡排序   a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
# for i in range(len(a)-1):
#     for j in range(0, len(a)-i-1): #和上面一样的，只是起始索引变了
#         if a[j] > a[j+1]:          #当j=0时，这里是第一个元素和第二个比较
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)




# dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
# for i in dict.keys():
#     print(i)
#2、请循环遍历出所有的value
# for i in dict.values():
#     print(i)
# 3、请在字典中增加一个键值对,"k4":"v4"
# dict1 = {"k4":"v4"}
# dict.update(dict1)
# print(dict)

# Friuts = {
# 	"苹果":12.3,  # 水果和单价
# 	"草莓":4.5,
#     "香蕉":6.3,
#     "葡萄":5.8,
#     "橘子":6.4,
#     "樱桃":15.8
# }
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money':
#     }
# }




#编写一个函数，传入一个列表，并统计每个数字出现的次数 返回字典数据：{21:3,56:9,10:3}
# list=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
# def all_list(list):
#     result = {}
#     for i in set(list):
#         result[i]=list.count(i)
#     return result
# print(all_list(list))

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# dict={}
# i=0
# #
# for i in names:
#     list_key=names[i][0]
#     list_value=names[i][1:]
#     dict(zip(list_key,list_value))
# employee=()
# for i in names:
#     employee[i[0]]=dict({"年龄":[1],
#                          "性别":[2],
#                          "编号":[3],
#                          "任职公司":[4],
#                          "薪资":[5],
#                          "部门编号":[6]})
#     print(employee)






