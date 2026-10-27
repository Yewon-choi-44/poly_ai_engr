import pandas as pd
import seaborn as sns

'''
df = sns.load_dataset('titanic')

'''
# 결측치 확인 및 ffill/dfill, drop
'''
df.info()

print(df['deck'].value_counts())
print(df['deck'].value_counts(dropna=False))


# 모든 열이 Null인 행이 있으면 True 반환
# e.g. survived 열의 모든 값이 null 이면 True
print(df.head(10).isnull().all())
print(df.head(10).isnull().any())

print(df.isnull().sum(axis=0)) # 하나의 열에 Null이 몇 개 있는지 체크
print(df.isnull().sum(axis=1)) # 한 행에 Null이 몇 개 있는지 체크
print(len(df) - df.count())

# drop, dropna, dropna(thresh)...
# 기본적으로 null 값이 채울 수 없을만큼 많은 경우는 반드시 삭제

df_drop = df.drop(columns = 'deck')
df_drop.info()
df_thresh = df.dropna(axis=1, thresh=500) # 하나의 열/행에 null 값이 500개 이상이면 해당 열/행을 삭제해주세요
# 온도 데이터가 20개 들어온느 케이스 23, 23.2, 23.4, ... 30.1
# Null이 5개 이상 안 들어오는 케이스는 뭔가 문제가 있는 거..
# df.dropna(axis=0, thresh=5)
print(df_thresh.head())

print(df[df['embarked'].isnull()])
print(df[df['embark_town'].isnull()])
df_ffill = df['embark_town'].ffill()
print(df_ffill[825:])
# bfill도 한 번 해보세요.
'''
#########################################################
#펭귄
'''
2. 중복 데이터 처리 (duplicated)/drop
'''

df = sns.load_dataset('penguins')
# print(df.head())
# print(df.info())
#
# print(df.isnull().sum())
# print(df.isnull().any(axis=1))
# print(df[df.isnull().any(axis=1)])

df_pg = df.drop(index=[3,339], columns='sex') # 3~339에 해당하는 컬럼을 삭제 할거다
# print(df_pg.isnull().any(axis=1)) # NaN 모두 삭제했으므로 Empty 결과 도출
# print(df_pg[df_pg.isnull().any(axis=1)]) # NaN 모두 삭제했으므로 Empty 결과 도출

# 중복 데이터 처리: duplicated()
# print(df_pg.duplicated())
# print(df_pg[df_pg.duplicated()])
#
# print(df_pg.tail(2))
# print(df_pg[df_pg.describe()])
# print(df_pg[df_pg['body_mass_g'] == df_pg['body_mass_g'].max()])

df_pg.loc[344] = df_pg.loc[237]
# print(df_pg.tail(2))
# print(df_pg[df_pg.duplicated()])

df_pg.drop_duplicates(inplace=True)
# print(df_pg[df_pg['body_mass_g'] == df_pg['body_mass_g'].max()])


##############################################################
"""
3. 이상치 데이터 확인 및 처리
추가적으로 box plot을 통해서 점검하는 것도 좋음
# z-score + box plot 을 통해서 이상치 제거.
"""

# z-score 사용 할 거임.
# 2-sigma 이상/이하인 데이터는 삭제

import numpy as np

print(np.mean(df_pg['body_mass_g']))
print(np.std(df_pg['body_mass_g']))
# mean : 4201.754385964912
# std : 800.781229238452
# 3400 ~ 5000 정도의 데이터가 일반적인 데이터로 보면 됨.

def outlier(df, col, z):
    return df[abs((df[col] - np.mean(df_pg[col]))/np.std(df_pg[col])) > z].index

print(df_pg.loc[outlier(df_pg, 'body_mass_g', 2)])


#############################################################
"""
4. 단위 통일 / 단위 변환, 데이터 타입 결정, 카테고리 변수 필요시 원-핫 인코딩(get_dummies.
정규화
#
추가적으로 box plot을 통해서 점검하는 것도 좋음
# z-score + box plot 을 통해서 이상치 제거.
"""



df = pd.read_csv('./auto-mpg.csv', header=None)
## print(df.head()
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', ' acceleration', 'model_year', 'origin', 'name']

# 단위 환산
# mpg(mile per gallon) to kpl(km per liter)
# 1마일 (유인물 참고)
# mpg to kpl = mpg * (1.69,,/3.78..)
mpg_to_kpl = 1.60934 / 3.78541
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head())

# 자료형 확정
print(np.where(df['horsepower']=='?'))
df['horsepower'] = df['horsepower'].replace('?',np.nan)
# df.replace({'horsepower':'?'}, np.nan, inplace=True)
# df['horsepower'].replace({df[df.loc['horsepower'== np.nan]]:'?'}, inplace=True)
df = df.dropna(subset=['horsepower'], axis=0)
df['horsepower'] = df['horsepower'].astype(float)
df.info()

#####################################################################
# 범주화, 카테고리 원핫, 정규화
# 유인물 코드로 실습해보고 정리할 것.

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut( x = df['horsepower'], # 데이터 배열
                       bins = bin_dividers,  # 경계값 리스트
                       labels = bin_names,   # bin 이름
                       include_lowest = True)   # 첫 경계값 포함

# horsepower 열, hp_bin 열의 첫 15행 출력
print(df[['horsepower', 'hp_bin']].head(15))

horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))

df.horsepower = df.horsepower/abs(df.horsepower.max())
print(df.horsepower.head())
print('\n')

print(df.horsepower.describe())



#############################################################################
#여기부터 0622(월) 데이터전처리실습

df = sns.load_dataset('titanic')
df = df.loc[:, ['age', 'fare']]
print(df.head())
