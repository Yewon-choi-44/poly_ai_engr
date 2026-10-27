import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import torch
import random
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import metrics

from my_train_test_split_lee import my_train_test_split

# 체크용
from sklearn.model_selection import train_test_split, KFold
from typing import Any

# precision, recall
def precision(tp, fp) :
       return tp / (tp + fp)

def recall(tp, fn) :
       return tp / (tp + fn)

RANDOM_SEED = 42

pd.set_option('display.max_columns', None)
t_data = sns.load_dataset("titanic")

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   survived     891 non-null    int64
 1   pclass       891 non-null    int64
 2   sex          891 non-null    object
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64
 5   parch        891 non-null    int64
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object
 8   class        891 non-null    category
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
None
"""

data_name = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone']
target_name = ['survived']

df = pd.DataFrame(t_data)


# 제거할거 제거합시다
# survived 는 target
# pclass는 원핫 인코딩 했으니까 제거
# sex는 who에 male, female, child 가 있어서 who 를 쓰고 sex 제거
# who는 원핫 인코딩 후 제거
# sibsp(자식 여부 같은데), parch, fare,는 체크
# embarked, embark_town 은 하나는 원 핫 인코딩 후 둘 다 제거
# alive 는 survived 랑 겹치니 제거

# 원 핫 인코딩 대상 : pclass(이미 했음), who, embarked, 
# 제거 대상 : sex, alive, embark_town, class, 
# 체크 대상 : sibsp, parch, fare, deck, alone, age, adult_male
# sibsp, parch 는 일단 제거 (가족관계를 설명하는 데이터셋)
# deck도 제거 (NaN 값이 너무 많음.)
# alone, age(생각보다 빈값이 많네... )는 일단 넣어보고 나중에 1순위로 빼기
# age 검색 결과 빈 값이 20%를 차지함. 나이가 중요할까?
# adult_male : 이미 bool 이고 그냥 넣어보자. 

# 데이터 체크 부터 합시다. 제거 대상은 제거할꺼니까 제외
# 원핫 인코딩 부터 : who(891), embarked(889) -> embarked 2개 빔
# 수업시간에 2개 추가하는거 배움. 

# df의 embarked 가 Null 인 데이터 필터링
# print(df[(df['embarked'].isnull())])

# 최빈도 (embarked: S, Q, C)의 클래스를 비어 있는 61, 829 에 NaN값 대신 넣음.
# print(len(df[(df['embarked'] == "S")])) # 644
# print(len(df[(df['embarked'] == "Q")])) # 77
# print(len(df[(df['embarked'] == "C")])) # 168

df.loc[[61, 829], 'embarked'] = "S"

# one-hot을 만들 떄 pd.get_dummies 사용하면 됨.
pclass_one_hot = pd.get_dummies(t_data["pclass"])
who_one_hot = pd.get_dummies(t_data['who'])
embarked_one_hot = pd.get_dummies(t_data['embarked'])


# print(pclass_one_hot.head())
# print(who_one_hot.head())
# print(embarked_one_hot.head())

# 일단 합치기
df = pd.concat([t_data, pclass_one_hot, who_one_hot, embarked_one_hot], axis=1)
df.columns = df.columns.astype(str)
df = df.drop(['sex', 'alive', 'embark_town', 'class', 'sibsp', 'parch', 'deck', 'age', 'pclass', 'embarked', 'who'], 
             axis=1)

# df_1 = df[(df['age'].isnull()) & (df['survived']==1)]
# df_2 = df[(df['age'].isnull()) & (df['survived']==0)]

# print(len(df_1))    # 52
# print(len(df_2))    # 125

# 나이의 중위값이 30이니까 30.0 으로 준다.
# 다음에는 age를 가진 데이터를 뺸다? 그럼 500개로 학습 및 테스트가 될까?
# age 데이터를 빼자.

# 들어가 있는 데이터셋 : fare, alone, adult_male, [pclass, who, embarked]

train_df = df.loc[: ,'fare':'S']
test_df = df[[target_name[0]]]
# train_df[target_name[0]] = test_df

df_1 = df.loc[: ,'fare':'S']
df_1[target_name[0]] = test_df

# print(train_df.head())
# print(test_df.head())
# print(type(test_df))


# data_split
# 테스트 데이터셋은 셔플 안시키지 않나?
train_X, test_X = my_train_test_split(train_df, test_size=0.2, random_state=RANDOM_SEED)
train_y, test_y = my_train_test_split(test_df, test_size=0.2, random_state=RANDOM_SEED, shuffle=False)

# print('train_X', len(train_X))
# print('test_X', len(test_X))
# print('train_y', len(train_y))
# print('test_y', len(test_y))

# 2. SVC 커널 변경, C, gamma 값 변경 등을 통해 성능 향상 시키기
# 2-1) 입력 데이터 다양화 (예: 성별, who, 칼럼 등을 포함해서 사용해보기)
# 2-2) svm 파아미터 변경
# 2-3) 그래도 잘 안나온다 ==> 구글링 해보시기 바랍니다.
# 2-4) kaggle 순위 높은 방법론들 찾아서 github에서 한 번 확인해보고 정리해보기

# 모델 선정 및 파라미터 세팅
# SVC : support vector classifier, SVR : Regression
svm_model = SVC(kernel='rbf', C=100, gamma='scale')


# 인공지능 모델 학습
# hyperlane : 생존 여부를 잘 판단할 수 있는 경계선을 찾기
svm_model.fit(train_X, train_y) 

# 3. svm_model.predict 결과를 활용하여
# - metrics.confusion_matrix 메서드 직접 구현해보기
# - metrics.classification_report 메서드 직접 구현
# 학습된 모델 파라미터로 추론 및 10개 데이터 확인
pred_y = svm_model.predict(test_X)
test_y = test_y.squeeze().to_numpy()
label_nums = len(set(test_y))

my_confusion_matrix = [[0 for _ in range(label_nums)] for _ in range(label_nums)]

for idx in range(len(test_y)) :
       my_confusion_matrix[test_y[idx]][pred_y[idx]] += 1

# 정답 0에 대한 지표 
tp0 = my_confusion_matrix[0][0]
fp0 = my_confusion_matrix[1][0]
fn0 = my_confusion_matrix[0][1]

pre0 = precision(tp0, fp0)
rec0 = recall(tp0, fn0)
# 정답 1에 대한 지표
tp1 = my_confusion_matrix[1][1]
fp1 = my_confusion_matrix[0][1]
fn1 = my_confusion_matrix[1][0]
pre1 = precision(tp1, fp1)
rec1 = recall(tp1, fn1)

print(f"\t\tprecision\trecall\n"

f"\t0\t{pre0:.2f}\t\t{rec0:.2f}\n"
f"\t1\t{pre1:.2f}\t\t{rec1:.2f}")

svm_matrix = metrics.confusion_matrix(test_y, pred_y)
print(svm_matrix)
print(metrics.classification_report(test_y, pred_y))
#exit()
# def svm_grid_search(model, df:pd.DataFrame, target_name: str, param_grid:dict, cv=5) :
#     data_split = int(df.shape[0]*(1/cv))

#     for d in range(cv) :
#         train_X = pd.concat([df.iloc[:data_split*d, :df.shape[1]-1], df.iloc[data_split*(d+1):, :df.shape[1]-1]])   # (16512,8)
#         train_y = pd.concat([df.iloc[:data_split*d, df.shape[1]-1], df.iloc[data_split*(d+1):, df.shape[1]-1]])
#         test_X = df.iloc[data_split*d:data_split*(d+1), :df.shape[1]-1]      # (4128, 8)
#         test_y = df.iloc[data_split*d:data_split*(d+1):, df.shape[1]-1]
        
#         for C in param_grid['C'] :
#             for gamma in param_grid['gamma'] :
#                 svm = model(C=C, gamma=gamma)
#                 svm.fit(train_X, train_y)
#                 pred_y = svm.predict(test_X)
#                 svm_matrix = metrics.confusion_matrix(test_y, pred_y)
#                 print(svm_matrix)
#                 print(metrics.classification_report(test_y, pred_y))




# 만약 최적의 결과값을 모르고 알아보고 싶다면 이하를 실행해주세요.


# gridsearchCV 를 구현하고 싶었는데 생각보다 어렵네요...허허...
cv = 5
param_grid = {'kernel' : ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
              'C' : [0.001, 0.01, 0.1, 1, 10, 100],
              'gamma' : [0.001, 0.01, 0.1, 1, 10, 100]}

svm_model2 = SVC()
data_split = int(df.shape[0]*(1/cv))

"""
confusion matrix
TP     FP
FN     TN
"""


total_score = 0
record_kernel = ''
record_C = 0
record_gam = 0
res_score = []
for d in range(cv) :
       train_X = pd.concat([df_1.iloc[:data_split*d, :df_1.shape[1]-1], df_1.iloc[data_split*(d+1):, :df_1.shape[1]-1]])   # (16512,8)
       train_y = pd.concat([df_1.iloc[:data_split*d, df_1.shape[1]-1], df_1.iloc[data_split*(d+1):, df_1.shape[1]-1]])
       test_X = df_1.iloc[data_split*d:data_split*(d+1), :df_1.shape[1]-1]      # (4128, 8)
       test_y = df_1.iloc[data_split*d:data_split*(d+1):, df_1.shape[1]-1]
       
       #for kernel in param_grid['kernel'] :
       for C in param_grid['C'] :
              for gamma in param_grid['gamma'] :
                     svm = SVC(C=C, gamma=gamma)
                     svm.fit(train_X, train_y)
                     pred_y = svm.predict(test_X)
                     svm_matrix = metrics.confusion_matrix(test_y, pred_y)
                     print(svm_matrix)

                     classification_report = metrics.classification_report(test_y, pred_y)
                     print(classification_report)
                     with open('metrics_classification_report.txt', 'a', encoding='utf-8') as f:
                            # f.write(svm_matrix)
                            f.write(classification_report)
                     # 정답 0에 대한 지표
                     tp0 = svm_matrix[0][0]
                     fp0 = svm_matrix[1][0]
                     fn0 = svm_matrix[0][1]

                     pre0 = precision(tp0, fp0)
                     rec0 = recall(tp0, fn0)
                     # 정답 1에 대한 지표
                     tp1 = svm_matrix[1][1]
                     fp1 = svm_matrix[0][1]
                     fn1 = svm_matrix[1][0]
                     pre1 = precision(tp1, fp1)
                     rec1 = recall(tp1, fn1)

                     pred_score = [pre0, rec0, pre1, rec1]
                     sum_pred_score = sum(pred_score)
                     if total_score < sum_pred_score :
                            total_score = sum_pred_score
                            record_C = C
                            record_gam = gamma
                            res_score = pred_score
                            final_report = classification_report

                     
with open('res_report.txt', 'w', encoding='utf-8') as f:
       f.write(f"optimal kernel : {record_kernel}\n")
       f.write(f"optimal C : {record_C}\n")
       f.write(f"optimal gamma : {record_gam}\n")
       f.write(f"final score : {res_score}\n")
       f.write(f"final report : \n{final_report}")