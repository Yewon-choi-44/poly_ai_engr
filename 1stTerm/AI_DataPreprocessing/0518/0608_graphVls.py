import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False


#########################################################
#########################################################

# df = pd.read_excel('./남북한발전전력량.xlsx')
# df.info()
# print(df.head(10))

#########################################################

'''
# columnL 1990~2015 --> 범례(라벨)
# 인덱스(row): x축
# value: y축

df_sn = df.iloc[[0,5], :]
print(df_sn.info)

#########################################################

# 먼저 이걸로 출력
# df_sn.plot()
# plt.show()

#########################################################

# 그 다음에 이거 시도
df_vis = df_sn.T
print(df_vis)
df_vis.columns = ['south', 'north']

exit()
df_vis.plot()
df_vis.plot(kind='bar')
df_vis.plot.barh()
plt.show()
'''

#########################################################
#########################################################
#########################################################
#########################################################


df = pd.read_csv("./auto-mpg.csv")
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']
#########################################################
# df_mpg = df['mpg']
# df_mpg.plot(kind='hist', bins=8)
# # df.plot(kind='scatter', x= 'weight', y='mpg')
# plt.show()
#########################################################

df_box = df[['mpg', 'cylinders']]
df_box.plot(kind='box')
plt.show()
