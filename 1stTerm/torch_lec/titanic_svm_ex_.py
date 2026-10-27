import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
t_data=sns.load_dataset('titanic')
print(t_data.head())
print(t_data.describe())
print(t_data.info())


df=t_data.drop(['deck', 'age', 'embark_town', 'alive','class'],axis=1)
#df의 embarked가 null인 거 필터링
print(df[(df['embarked'].isnull())]) #61, 829
#최빈도(embarked: S,Q,C)의 클래스를 비어있는 61, 829번에 입력
print(len)
