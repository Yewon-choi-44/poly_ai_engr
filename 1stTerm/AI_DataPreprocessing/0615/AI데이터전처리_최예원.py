import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
#
# df=pd.read_csv("./Pokemon.csv")
# print(df)
# print(df.info())
#
# df_atk = df.sort_values(by='Attack', ascending=False)
#
# df_atkLegend = df_atk.loc[df['Legendary']]
# print(len(df_atkLegend))
# df_atk[]
# # print(df_atkLegend.iloc[401:800])


'''
#2
df_fire = df.loc[df['Type 1']=='Fire']
print((df_fire['Attack']).mean())
fire_mean = df_fire['Attack'].mean()

df_water = df.loc[df['Type 1']=='Water']
print(len(df_water.loc[df['Attack']>=fire_mean]))
'''


#3.

df3 = pd.read_csv('./bank.csv')

print(type(df3))
print(df3)
# print(len(df3.loc[df3['y']=='yes']))
# df3_yes = df3.loc[df3['y']=='yes']
# print(df3_yes)
# print(df3_yes['age']<10)
print(len(df3.loc[(df3['age']<30) & (df3['age']>=20)])) #478
print(len(df3.loc[(df3['age']<20) & (df3['age']>=10)])) # 4
print(len(df3.loc[(df3['age']<10) & (df3['age']>=0)])) # 0


#4
df3_2529 = df3.loc[(df3['age']<29) & (df3['age']>=25)]
print(len(df3_2529.loc[df3_2529['housing']=='yes'])) #187


# print(df3.loc[df3['age']<20 & df3['age']>=10])
# print(df3.loc[df3['age']<30 & df3['age']>=20])


#5.
print(df3['balance'].mean())
df5_balMean = df3['balance'].mean() #1422.6578190665782
print(df3.loc[df3['balance']>=df5_balMean])

df3_bal = df3.loc[df3['balance']>=df5_balMean]
df3_balSort = df3_bal.sort_values(by='balance', ascending=False)

print(len(df3_balSort['balance'][:100]))
print(df3_balSort['balance'][:100].mean()) #16029.52


# df3_yes_10 = df3_yes.loc[df3_yes['age']<10]
# print(df3_yes_10)
# print(df3_yes.loc[df3_yes['age']<10])

print()


#6.
print(df3['contact'])
df6=df3.loc[(df3['contact']=='telephone') | (df3['contact']=='cellular')]
print(df6)
print(df6['day' ].mode())
print(df6['month'].mode())
# print(df6.loc[(df6['month'].mode())& (df6['day'].mode())])
print(df6[['day', 'month']].mode())


#7.
print(df3['age'].corr(df3['age'])) #1.0
print(df3['age'].corr(df3['balance']))#0.08382014224477764
print(df3['balance'].corr(df3['age'])) #0.08382014224477764
print(df3['balance'].corr(df3['balance'])) #1.0


# 8.

df8 = pd.read_csv('./healthcare-dataset-stroke-data.csv')
print(df8.head(10))
df8_male= df8.loc[df8['gender']=='Male']
print(df8_male.head(10))
print(df8_male['age'].mean())  #42.483385342789596

#9.
df8 = df8.fillna(df8['bmi'].mean())
print(df8['bmi'].mean()) #28.893236911794663

#10.
df10 = pd.read_csv('./healthcare-dataset-stroke-data.csv')
# df10['bmi'].mean()

df10_010 = df10.loc[(df10['age']<10) & (df10['age']>=0)]
df10_1020 = df10.loc[(df10['age']<20) & (df10['age']>=10)]
df10_2030 = df10.loc[(df10['age']<30) & (df10['age']>=20)]

print(df10_010['bmi'].mean())
print(df10_1020['bmi'].mean())
print(df10_2030['bmi'].mean())


df10.loc[df10['age']<10].fillna(df10['bmi'].mean())
df10.loc[(df10['age']<20) & (df10['age']>=10)].fillna(df10_1020['bmi'].mean())
df10.loc[(df10['age']<30) & (df10['age']>=20)].fillna(df10_2030['bmi'].mean() )
print(df10)