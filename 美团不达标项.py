import pandas as pd

df = pd.read_excel(r"咖啡店日均尾部履约问题改善.xlsx")

all_action = []
for item in df['美团不达标项'].dropna():
    action = item.split(',')
    action = [i.replace(r'\s+','') for i in action]
    action = [i.strip() for i in action]
    all_action.extend(action)
action_series = pd.Series(all_action,name = '美团不达标项')
counts = action_series.value_counts()
percentage = action_series.value_counts(normalize = True)
result = pd.merge(counts,percentage,on = '美团不达标项',how = 'inner')
result = result.rename(columns = {
    'count':'数量',
    'proportion':'占比'
})

result['level'] = result['数量'].apply(lambda x: 'L1' if x >= 10 else 'L2' if x >= 5 else 'L3')
result = result.reset_index(drop = False)


result['满意度'] = result['美团不达标项'].apply(lambda x : '是' if '满意度' in x else '否')
result['率'] = result['美团不达标项'].str.contains('率',na = False).map({True:'是',False:'否'})
mask = result.apply(lambda x : x.astype(str).str.contains('反馈率',na = False).any(),axis = 0)