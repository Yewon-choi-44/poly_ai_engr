import pandas as pd
import seaborn as sns

#from check_setting_env import df

pd.set_option('display.max_columns', None)
t_data = sns.load_dataset('titanic')
# print(type(t_data))
print(t_data.head())
print(t_data.info())

# one-hot을 만들 때 pd.get_dummies 사용하면 됨.
pclass_one_hot = pd.get_dummies(t_data.pclass)
print(pclass_one_hot.head())

# Boolean Indexing <-- 중요합니다. 꼭 이해도 하시고 여러 조건을 걸어서 결과 확인해보세요.
# 설명만 했네요.(실습)
# df(대괄호안에 조건을 넣으면 됩니다)
df_0 = t_data[(t_data['survived']==0)]
df_1 = t_data[(t_data['survived']==1)]
# survived == 1 and age >= 30
df_2 = t_data[(t_data['survived']==1) & (t_data['age']>=30)]
print(len(df_0), len(df_1), len(df_2))

# concat : data frame 끼리 붙이기
# axis 0/1 차이점 확인해볼것
df = pd.concat([t_data, pclass_one_hot], axis=1)
print(df.tail())
df = t_data.drop(['deck','age','embark_town','alive', 'class'],axis=1)
# df의 embarked 가 null 인거 필터링
print(df[(df['embarked'].isnull())]) # 61, 829
# 최빈도 (embarked: S,Q,C)의 클래스를 비어있는 61, 829 번에 입력
print(len(df[(df['embarked']=='S')]), len(df[(df['embarked']=='Q')]),
      len(df[(df['embarked']=='C')]))

df.loc[[61, 829], 'embarked'] = 'S'
print(df[(df['embarked'].isnull())]) # None

# exit()
# 여러분이 나중에 sex, who 컬럼의 값에 따라 str ==> int로 변경
"""
for idx, val in enumerate(df['who']): 
    if val == 'man': df['who_int'] = 0
    if val == 'woman': df['who_int'] = 1
    if val == 'child': df['who_int'] = 2
"""
# 데이터 날리기
df.drop(['sex', 'who', 'embarked'], axis=1, inplace=True)
print(df.head())

# embarked <-- 카테고리니깐 원-핫으로 변경해서 입력 데이터로 사용해 볼 것
# 학습 데이터 준비

x = df.loc[:, 'pclass':'alone']
y = df['survived']

# 학습 및 평가를 위해 데이터 셋 분리
from sklearn.model_selection import train_test_split
# pip install scikit-learn 이걸 터미널에서 설치하기
x_train, x_test,y_train,  y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 모델 선정 및 파라미터 셋팅
from sklearn.svm import SVC

# 인공지능 모델 학습
svm_model = SVC(kernel='rbf', C=10000, gamma=100.0)
svm_model.fit(x_train, y_train)
# 학습된 모델 파라미터로 추론 및 10개 데이터 확인
y_pred = svm_model.predict(x_test)
print(y_pred[0:10]) #[0,0,0...0]으로 예측
print(y_test[0:10]) #[1,0,0,1,1...0]으로 예측

# 22페이지에 보면 성능평가
from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_pred)
print(svm_matrix)
print(metrics.classification_report(y_test, y_pred))