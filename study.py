import pandas as pd

df = pd.read_excel(r"1.1-1.11咖啡店日均尾部门店履约问题改善.xlsx")

all_option = []
for item in df['美团不达标项'].dropna():
    option = item.split(',')
    option = [i.strip() for i in option]
    all_option.extend(option)
series = pd.Series(all_option,name = '美团不达标项')
counts = series.value_counts().rename('数量')
percentage = series.value_counts(normalize=True).rename('占比')
merged = pd.merge(counts,percentage,on = '美团不达标项',how = 'inner').reset_index()

idx = merged[merged['美团不达标项'] == '复购率'].index
df2 = merged.drop(index = idx)
idx_max = df2['数量'].idxmax()
mask = merged['数量'].apply(lambda x : x > 10)
idx3 = mask.idxmax()
merged['数量'] = merged['数量'].astype(int)
mask2 = merged.apply(lambda x : x.astype(str).str.contains('率',na = False).any(),axis = 1)
max_value = mask2.max()
id4 = mask2[mask2 == max_value].index
idx6 = []
for item in merged['数量']:
    if item > 5:
        idx5 = merged[merged['数量'] == item].index
        print(idx5[0])
        idx6.append(idx5[0])
        print(idx6)
df3 = merged.loc[idx6]

idx8 = []
for item in merged['美团不达标项']:
    if '满意度' in item:
        idx7 = merged[merged['美团不达标项'] == item].index
        print(idx7)
        idx8.extend(idx7)
df5 = merged.loc[idx8]

# 对于字符串判断是否含有某子串，用in 判断，str.contains()是pandas中的用法，适用于series和dataframe
mask3 = merged['美团不达标项'].apply(lambda x : '满意度' in x)

# str.contains()是pandas中的用法，适用于series和dataframe，返回一个series或dataframe的bool值
mask3_ = merged['美团不达标项'].str.contains('满意度')
idx9 = mask3[mask3 == max(mask3)].index   # 这种方法可获取series最大值对应的索引，若有多个最大值，则返回所有最大值对应的索引
idx10 = mask3.idxmax()                    # idxmax()可获取series最大值对应的索引,但若有多个最大值，则返回第一个最大值对应的索引
df6 = merged.loc[idx9]
max_ = max(df6['数量'])

mask4_1 = merged.apply(lambda x : x.astype(str).str.contains('满意度',na = False).any(),axis = 1) # 性能更好
mask4_2 = merged.apply(lambda x : x.astype(str).str.contains('满意度',na = False)).any(axis = 1)
mask5 = merged.apply(lambda x : x.astype(str).str.contains('满意度',na = False)).any(axis = 0)

merged['level'] = merged['数量'].apply(lambda x : 'L1' if x > 10 else 'L2' if x >= 5 else 'L3')
merged['满意度'] = merged['美团不达标项'].str.contains('满意度',na =  False).map({True:'是',False:'否'})
merged['率'] = merged['美团不达标项'].apply(lambda x : '是' if '率' in x else '率  率')
merged = merged.apply(lambda x : x.replace(r'[a-zA-Z]','',regex = True))
df7 = pd.DataFrame({
    'A': [True, False],
    'B': [False, False]
})
mask6 = df7.any(axis = 1)