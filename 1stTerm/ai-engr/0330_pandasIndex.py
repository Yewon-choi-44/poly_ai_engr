import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[5,4,6], 'c2':[7,8,9]}
df = pd.DataFrame(dict_data)
print()
print(df)

sorted_df = df.sort_values(by='c1', ascending=False) #ascending=False -> 오름차순으로 뽑겠다
print()
print(sorted_df)