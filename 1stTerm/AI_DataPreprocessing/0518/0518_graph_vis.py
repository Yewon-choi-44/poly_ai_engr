import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0518/sell_bike.csv", encoding='cp949', index_col='자전거매장')
print(df)


##############################세로 바 그래프################################
# x축: 자전거매장, y축: Data, 범례: 컬럼(1월~6월)
# df.plot(kind='bar')
# plt.show()

# index = [1, 2, 3, 4, 5, 6]
# London = list(df.loc['런던'].values)
# York = list(df.loc['요크'].values)
# L_450 = []
# for val in London:
#     if val >= 450:
#         L_450.append(val)
#     else:
#         L_450.append(0)
#
# # 요크는 list 중첩으로 한 번 구현...
# Y_450 = [val if val<=450  else 0 for val in York]
# print(Y_450)
#
#
# plt.subplot(2, 1, 1)
# plt.bar(index, London, color='brown')
# plt.bar(index, L_450, color='orange')
# plt.legend(['No','Yes'], loc='best')
# plt.axhline(y=450, xmin=0, xmax=1, color='blue') #min, max: 0, 1 (0~1 사이 비율로 작성)
# plt.ylabel('London')
# plt.ylim(0, 1200)
#
# plt.subplot(2, 1, 1)
# plt.bar(index, York, color = 'orange')
# plt.bar(index, Y_450, color = 'brown')
# plt.axhline(y=450, xmin=0, xmax=1, color='blue') #min, max: 0, 1 (0~1 사이 비율로 작성)
# plt.ylabel('York')
# plt.ylim(0, 1200)
#
#
#
# # plt.subplot(2, 1, 1)
# # plt.bar(index, London, color='brown',axis=1)
# # plt.legend(['No','Yes'], loc='best')
# # plt.ylabel('No')
# # plt.ylim(0,1200)
#
# plt.show()
#



######################################가로 바그래프#############################################
# index = ['yes','np']
# # print(df[df >= 450].count().sum()) #이렇게 하면 boolean형 인덱싱...으로 조건을 걸 수 있다고 말씀하셨다고 한다...
# # print(df[df < 450].count().sum())
# yes_cnt = df[df >= 450].count().sum()
# no_cnt = df[df < 450].count().sum()
# print(yes_cnt, no_cnt)
# y_data =[yes_cnt, 0]
# plt.barh(index, y_data, color='orange', height=0.6)
# y_data=[0, no_cnt]
# plt.barh(index, y_data, color='brown')
# plt.show()
########################################################################
'''
df_sum = df.sum(axis=1)
df_sum.sort_values(axis=0, inplace=True)
df_sum.plot(kind='barh', grid=True)
# print(df_sum)
# df_sum.plot(kind='barh')
# df,sum.plot.barh() <- 위에 거랑 이거랑 같은 거니가 맘에 드는 거 쓰면 댐
plt.xlim(2200, 3500)
# plt.xticks(rotation=90) # x축 눈금 글씨를 90도 옆으로 회전 하는 옵셩
plt.xticks(list(range(2200, 3500, 100)))
plt.show()
'''


####################여기부턴 sell_bike_inc_kinds.csv로.#####################################
df1 = pd.read_csv("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0518/sell_bike_inc_kinds.csv", encoding='cp949', index_col='자전거매장')

print(df1)
# df1.plot.barh(color=["#000000","#555555","#199997"], stacked)

df_trans = df.T
df1_trans = df1.T
'''
# print(df1_trans)
plt.subplot(3,1,1)
df1_trans.plot(kind='barh', color=["#554534", "#AAAAAA","#CCCCCC"], stacked=True)
# plt.xticks(rotation=90)
plt.subplot(3,1,2)
df1_trans.plot(kind='barh', color=["#000000","#199997","#CCCCCC"], stacked=True)
plt.subplot(3,1,3)
df_trans.subplot(kind='barh', color=["#554534", "#AAAAAA","#CCCCCC"], stacked=True)
# df2_trans.plot(kind='barh', color=["#554534", "#AAAAAA","#CCCCCC"], stacked=True)
# plt.xticks(rotation=90)
plt.show()
'''

################################
'''
ax = plt.subplot(2,1,1)
# df.plt.barh(x, y, stacked=True)
df.plot.barh(ax=ax, color=["#000000", "#555555", "#AAAAAA"], stacked=True)
axes = plt.subplot(2,1,2)
df1_trans.plot(ax=axes, kind='barh', color=["#000000", "#555555", "#AAAAAA"], stacked=True)
plt.show()
'''
fig, axes_ = plt.subplots(nrows=2, ncols=1) #얘는,,,
df.plot.barh(ax=axes_[0], color=["#000000", "#555555", "#AAAAAA"], stacked=True)
df_trans.plot(ax=axes_[1], kind='barh', color=["#000000", "#CCCFFF", "#AAACCA"], stacked=True)
plt.show()