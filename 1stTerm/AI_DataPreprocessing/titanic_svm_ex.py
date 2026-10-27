import pandas as pd
import seaborn as sns #matploylib (시각화 할때)
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
pd.set_option('display.max_columns', None)
t_data = sns.load_dataset('titanic')
print(t_data.head())
print(t_data.info())

print(type(t_data))
print(t_data.head())
print(t_data.info())

#one-hot을 만들 때 pd.get_dummies 사용하면 됨.
pclss_one_hot = pd.get_dummies(t_data.pclass)
print(pclss_one_hot.head())

# Boolean Indexing
# <-- 중요합니다. 꼭 이해도 하시고 여러 조건을 걸어서 결과 확인해보세요.
# 설명만 했네요.(실습)
# df[ (대괄호 안에 조건을 넣으면 됩니다.) ]
df_0 = t_data[(t_data['survived']==0)]
df_1 = t_data[(t_data['survived']==1)]
# survived==1 and age >=30
df_2 = t_data[(t_data['survived']==1) & (t_data['age']>=30)]
print(len(df_0), len(df_1), len(df_2))

# concat : data frame 끼리 붙이기
df = pd.concat([t_data, pclss_one_hot], axis=1)
df = pd.concat([t_data, pclss_one_hot], axis=1)
print(df.tail())
df = t_data.drop(['deck', 'age', 'embark_town', 'alive', 'class'], axis=1)

# df의 embarked 가 null 인거 필터링
print(df[(df['embarked'].isnull())]) # 61, 829
# 최빈도 (embarked: S, Q, C) 의 클래스를 비어 있는 61, 829 번에 입력
print(len(df[(df['embarked']=='S')]), len(df[(df['embarked']=='Q')]),
      len(df[(df['embarked']=='C')]))

df.loc[[61, 829], 'embarked'] = 'S'
print(df[(df['embarked'].isnull())]) # None


# 여러분이 나중에 sex, who 컬럼의 값에 따라 str ==> int로 변경

for idx, val in enumerate(df['who']):
  if val == 'man': df['who_int'] = 0
  if val == 'woman': df['who_int'] = 1
  if val == 'child': df['who_int'] = 2


df.drop(['sex', 'who', 'embarked'], axis=1, inplace=True)
print(df.head())
# embarked <-- 카테고리니깐 "원-핫"으로 변경해서 입력 데이터로 사용해 볼 것

# 학습 데이터 준비 # ==> 우리는 지금 지도학습으로 생존여부를 판단하고자 함.
x = df.loc[:, 'pclass':'alone']
y = df['survived']

# 1. 데이터 split을 함수로 구현 (기존에 랜덤하게 70%는 train, 30%는 test)
# - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할 지 받아서 처리할 것
# 학습 및 평가를 위해 데이터 셋 분리 (과제로도 수행을 했었음)
x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=42))
# random state: 42 ==> 0,1,2,3,4,5,7  test: 6,8,9
# random state: 77 ==> 1,2,3,4,5,6,7  test: 0,8,9
# radom seed == random state

# 2. SVC 커널 변경, C, gamma 값 변경 등을 통해 성능 향상 시키기(2-1, 2-2: mandatory)
# 2-1) 입력 데이터 다양화(예: 성별, who 컬럼 등 포함해서 사용해보기)
# 2-2) svm 파라미터 변경
# 2-3) 그래도 잘 안나온다..==> 구글링 해보시기 바랍니다.
# 2-4) kaggle 순위 높은 방법론들 찾아서 github에서 한 번 확인해보고 정리해보기

# 모델 선정 및 파라미터 셋팅
svm_model = SVC(kernel='rbf', C=0.1, gamma=10.0)

# 인공지능 모델 학습
# hyperplane: 도출 생존여부를 잘 판단할 수 있는 경계선을 찾았음
svm_model.fit(x_train, y_train)

# 3. svm_model.predict 결과를 활용하여
# - metrics.confusion_matrix 메서드 직접 구현해보기.
# - metrics.classification_report 메서드 직접 구현.
# 학습된 모델 파라미터로 추론 및 10개 데이터 확인
y_pred = svm_model.predict(x_test)
# print(y_pred[0:10]) # [0, 0, 1, 0, 1]
# print(y_test[0:10]) # [1, 0, 0, 1, 1]

from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_pred)
print(svm_matrix)
print(metrics.classification_report(y_test, y_pred))


