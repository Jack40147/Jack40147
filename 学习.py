import math
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = math.sqrt(9)
print(a)
import numpy
b = np.sqrt(9)
print(b)

# 数字类型 + - * / % // ** int(整数) float（浮点数）
age = 20.0
print(age + 1)
print(type(age))

# 字符串str
name = '小明'
print(type(name))

# 拼接
print("你好",name)
# 长度(len)
print(len(name))

# 索引
print(name[1])
print(name[0:2])
print(name[:2])
print(name[-1])
print(name.index("小"))

# 大小写转换 lower(小写) upper（大写）
s = "Python"
print(s.lower())
print(s.upper())

# 替换replace
print(s.replace("Python", "Java"))
a = '全 国'
print(a.replace(" ",""))

# 分割split（得到一个列表）
s2 = "苹果,香蕉,橘子"
print(s2.split(","))

# 判断开头和结尾 startswith endswith
print("数据.xlsx".endswith(".xlsx"))

# 去除字符串前后空格strip


# 类型转换
num = '123'
print(type(num))
num = int(num)
print(type(num))
num = str(num)
num = float(num)

# 列表
fruits = ['苹果','香蕉','橘子']
# 查
print(fruits[0])
print(fruits[0:2])
idx = fruits.index('橘子')
# 更改
fruits[0] = '葡萄'
print(fruits)
# 添加元素
fruits.append('桃子')
fruits.insert(0,'柠檬')

# 删除
fruits.pop()
fruits.remove('葡萄')

del fruits[1]

# 字典
# 定义一个字典{}
student = {
    "name":"小明",
    "age":22,
    "score":[90,80,98],
    "is_student":True
}
# 查
name = student["name"]
print(name)
age = student.get("age") # 键不存在时会返回None，不会报错
gender = student.get("gender")
print(gender)

# 改
student['age'] = 23
print(age)
# 增加
student['gender'] = '男'
print(student)
# 删除
student.pop("age")
print(student)
del student["gender"]
# 取所有的键
print(student.keys())
print(student.values())


#========================循环遍历========================

for i in range(0,10,2):
    a = i+1
    print(a)


# 遍历字符串
for i in s:
    print(i)

# 遍历列表
for fruit in fruits:
    print(fruit)

for index,fruit in enumerate(fruits):
    print(f"索引为{index}的是{fruit}")

# 遍历字典
dic = {
    "小明":"男",
    "小红":"女",
}
for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)
for key,value in dic.items():
    print(f"{key}的性别为{value}")

# ============================os库============================
import os
# 获取当前工作目录
print(os.getcwd())

# 遍历文件夹中的文件listdir
filenames = os.listdir(r"E:/pycharmprofessionalproject/study/各地区城市商品零售价格分类指数")
print(filenames)
for filename in filenames:
    print(filename)

# 路径拼接os.path.join
for filename in filenames:
    filepath = os.path.join(r"E:/pycharmprofessionalproject/study",filename)


# 判断文件夹是否存在os.path.exists
if os.path.exists("2004.xls"):
    print("存在")
else:
    print("不存在")

# 创建文件夹os.makedirs
if os.path.exists("raw"):
    print("存在")
else:
    os.makedirs("raw")

# 获取文件属性（拆分文件名和后缀）
filename_list = os.listdir(r"E:\pycharmprofessionalproject\study\各地区城市商品零售价格分类指数")
for filename in filename_list:
    name = os.path.splitext(filename)[0]
    print(name)

for filename in filenames:
    name = filename.split(".")[0]
    print(name)

# =========================pandas=========================

import pandas as pd

# 读取数据
# 1.相对路径
df = pd.read_excel("2004.xls")

# 2.绝对路径
df2 = pd.read_excel(r"C:\Users\Lenovo\Desktop\年度数据.xls")

# 指定工作表
df3 = pd.read_excel(r"E:\pycharmprofessionalproject\居民家庭隐含能\1992-2020现价表.xlsx",
                    sheet_name="2010",header=2,skiprows=2,dtype={"省份":str,"燃料":float})


# 查询和筛选
data = {
    "姓名":["张三","李四","王五","赵六"],
    "年龄":[20,32,12,45],
    "省份":["陕西","江苏","河南","山东"]
}
df4 = pd.DataFrame(data)
# 筛选数据
df5 = df4[["姓名"]]
df5 = df4.loc[:,["姓名","年龄"]]
df5 = df4.loc[1:2,["姓名","年龄"]]

df5 = df4.iloc[0]
df5 = df4.iloc[:,0]

# 条件筛选
df5 = df4[(df4["年龄"] > 20) & (df4["省份"] == "江苏")]

region = ["江苏","山东"]
df5 = df4[df4["省份"].isin(region)]

df5 = df4[df4["姓名"].str.contains("张")]

# 获取列索引df.columns
column_list = df4.columns.tolist()
print(column_list)
index_age = column_list.index("年龄")
print(index_age)
index_name = df4.columns.get_loc("姓名")

df6 = df4.iloc[:,[index_name,index_age]]

# 获取行索引
index1 = df4[df4["省份"] == "江苏"].index
print(index1[0])

# drop用法，去除不想要的数据
# df.drop(
#     labels =  None,
#     axis = 0或1
#     index,
#     columns = None,
#     inplace,True或者False
#     errors = 'raise' ignore 忽略
# )

df6 = df4.drop(columns=["省份"])
df6 = df4.drop(index = [0])

drop_index = df4[(df4["年龄"] > 20) & (df4["省份"] == "江苏")].index
print(drop_index)
df6 = df4.drop(index = drop_index)

# 数据类型转变换
# 查看数据类型(dtypes)
print(df4.dtypes)

# 类型转换
df4["年龄"] = df4["年龄"].astype(float)
df4["年龄"] = df4["年龄"].astype(int)
df4["年龄"] = df4["年龄"].astype(str)
df4["年龄"] = df4["年龄"].astype(int)

df4["年龄"] = pd.to_numeric(df4["年龄"],errors="coerce").astype('Int64')

# 缺失值处理
data = {
    "姓名":["张三","李四","赵六"],
    "年龄":[20,12,32],
    "省份":["陕西","山东","广东"],
    "收入":[5000,8000,7000]
}
df4 = pd.DataFrame(data)

df4 = df4.dropna()
# 缺失值填充
df4 = df4.fillna(0)

df4["年龄"] = df4["年龄"].astype(str).apply(lambda x: x.replace(" ","None"))
df5 = df4.fillna({
    "姓名":"未知",
    # "年龄":df4["年龄"].mean(),
    "省份":"未知",
    "收入":df4["收入"].median()
})

# 添加计算列
df4["收入"] = df4["收入"].astype(float)
df4["支出"] = df4["收入"] * 0.5
df4["余额"] = df4["收入"] - df4["支出"]

# 排序
df4 = df4.sort_values(by=["收入"],ascending=False)
df4 = df4.sort_values(by=["省份","年份"],ascending = [True,False])

# 数据合并merge，concat
df1 = pd.DataFrame({
    "ID":["001","002","003","004"],
    "收入":[30000,20001,20002,20003],
})
df2 = pd.DataFrame({
    "员工ID":["001","002","003","004"],
    "部门":["销售","技术","市场","技术"]
})
df3 = pd.DataFrame({
    "员工ID":["001","002","003","004"],
    "姓名":["zhang","li","zhao","wu"]
})
df4 = pd.DataFrame({
    "ID":["005","006","007","008"],
    "收入":[30000,20001,20002,20003]
})

merged = pd.merge(df1,df2,on = "员工ID",how = "inner")
merge = [df1,df2,df3]
result = merge[0]
for df in merge[1:]:
    result = pd.merge(result,df,on = "员工ID",how = "inner")

merge = pd.merge(df1,df2,left_on = "ID",right_on = "员工ID",how = "inner")

# concat
df_concat = pd.concat([df1,df4])

# ======================函数定义及调用===================
# 定义一个无参数、无返回值函数
def greet():
    print("你好！")
greet()

def greet_person(name):
    print(f"你好{name}!")
greet_person("老师")

# 定义一个有返回值的函数
def add(a,b):
    # 计算两个数的和
    result = a +b
    return result
add(a = 1,b = 2)

def proceed_file(filepath):
    df = pd.read_excel(filepath)
    return df
proceed_file("2004.xls")

# ======================打开一个excel中的所有sheet======================
excel_file = pd.ExcelFile(r"E:\pycharmprofessionalproject\居民家庭隐含能\1992-2020现价表.xlsx")
sheet_names = excel_file.sheet_names
print(sheet_names)
all_data = []
dic = {}
for sheet_name in sheet_names:
    df7 = pd.read_excel(r"E:\pycharmprofessionalproject\居民家庭隐含能\1992-2020现价表.xlsx",sheet_name=sheet_name)
    df7 = df7.iloc[0:42,1:43]
    dic[sheet_name] = df7
    # all_data.append(df7)
result = all_data[0]
for df in all_data[1:]:
    result = pd.merge(result,df,on = "<UNK>ID",how = "inner")

    filepath = os.path.join(r"E:\pycharmprofessionalproject\study\cleaned",f"{sheet_name}投入产出表.xlsx")
    df7.to_excel(filepath,index = False)

# ======================打开一个文件夹中的所有excel======================
filenames = os.listdir(r"E:\pycharmprofessionalproject\study\各地区城市商品零售价格分类指数")
for filename in filenames:
    filepath = os.path.join(r"E:\pycharmprofessionalproject\study\各地区城市商品零售价格分类指数",filename)
    df8 = pd.read_excel(filepath,header=None)
    keyword = "燃料"
    bool_matrix = df8.astype(str).apply(lambda x: x.str.contains(keyword,na=False))
    target = bool_matrix.any(axis=1)
    idx = df8[target].index
    columns = df8.iloc[idx[0]]
    df8.columns = columns
    df8 = df8.iloc[idx[0] + 1:]
    df8.columns = df8.columns.str.replace(" ", "")
    index_region = [index for index, column in enumerate(df8.columns) if "地区" in column]
    index_fuel = [index for index, column in enumerate(df8.columns) if "燃料" in column]
    df8 = df8.iloc[:, [index_region[0], index_fuel[0]]]
    df8.columns = ["地区", "燃料"]
    df8 = df8.reset_index(drop=True)
    df8 = df8.drop(index = 0)
    df8["地区"] = df8["地区"].apply(lambda x : x.replace(" ",""))
    df8["燃料"] = pd.to_numeric(df8["燃料"])
    filename = filename.split(".")[0]
    filepath = os.path.join(r"E:\pycharmprofessionalproject\study\cleaned\燃料价格指数",f"{filename}燃料价格指数.xlsx")
    df8.to_excel(filepath,index = False)


