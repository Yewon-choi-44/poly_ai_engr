import pandas as pd
import seaborn as sns
import torch
import numpy as np

pd.set_option('display.max_columns', None)
t_data = sns.load_dataset("titanic")
# print("------------t_data.head()------------")
# print(t_data.head())
# print("++++++++++++++++++++++++++++++++++++++++++")
# print()
# print()
# print("------------t_data.info()------------")
# print(t_data.info())
# print()
# print()

# pclass, sex, embarked, who 컬럼 one-hot encoding
pclass_one_hot = pd.get_dummies(t_data.pclass, prefix = 'pclass')
sex_one_hot = pd.get_dummies(t_data.sex, prefix = 'sex')
who_one_hot = pd.get_dummies(t_data.who, prefix = 'who')
df1 = pd.concat([t_data, pclass_one_hot, sex_one_hot, who_one_hot], axis = 1)

# 결측치 처리과정: df의 embarked가 null인거 필터링
# print("----- <df_del의 null인 행 확인하기> -----")
# print(df_del[(df_del['embarked'].isnull())])
# print()
# print()
# print("----- <embarked 컬럼별 행 개수> -----")
# print(len(df_del[(df_del['embarked']=='S')]), len(df_del[(df_del['embarked']=='Q')]), len(df_del[(df_del['embarked']=='C')]))
# print()
# print()

df1.loc[[61, 829], 'embarked']='s'
# print("----- <df1의 null 인 행 다시 확인하기> -----")
# print(df1[(df1['embarked'].isnull())])
embarked_one_hot = pd.get_dummies(t_data.embarked, prefix = 'embarked')
df1 = pd.concat([df1, embarked_one_hot], axis = 1)
df1 = df1.drop(['deck', 'alive', 'class', 'embark_town', 'pclass', 'sex', 'who', 'embarked', 'adult_male'], axis=1)
# df1.to_excel('hw_4.xlsx', index=False) #파일 전체 보기 위해서 엑셀로 내보내기 하는 코드!

df_avr = df1.fillna(df1['age'].mean())   #age 결측치를 age 열의 평균값으로 채움
# print(len(df_avr[(df_avr['age'].isnull())]))      #null 값 없는 것 확인


    # 1번. 데이터 split을 함수로 구현
# 데이터 섞는 것을 함수로 구현함
def randFun(num, dataFrame):
    # 무작위 번호를 뽑는 규칙을 정함
    torch.manual_seed(num)
    # 데이터 개수만큼의 숫자를 무작위로 나열한 번호표 리스트를 만듦
    idx = torch.randperm(len(dataFrame))
    # 무작위 번호표 순서대로 데이터 위치를 재배치 함
    shuffled = dataFrame.iloc[idx]
    return shuffled

# 데이터 split을 함수로 구현함 ==> 따로 파일 만들었으므로 모듈 import하고 함수 부름
import split_dataset_jung as s
df_shuffled = randFun(42, df_avr)
x_train, y_train, x_test, y_test = s.splitFun(0.7, df_shuffled)
# x_test.to_excel('x_test_1.xlsx', index=False)
# y_test.to_excel('y_test_1.xlsx', index=False)

# # randperm 및 데이터 split 결과 확인
# print(x_train.head())
# print("=====================================")
# print(y_train.head())
# print("=====================================")
# print(x_test.head())
# print("=====================================")
# print(y_test.head())


# SVM 모델 파라미터 설정함
from sklearn.svm import SVC
svm_linear = SVC(kernel='linear', C=1.0, gamma=10.0)
svm_linear.fit(x_train, y_train) #머신러닝 모델이 데이터를 보고 **학습(Training)**을 수행하는 핵심 단계
# fit (학습): 문제집(x_train)과 해설지(y_train)를 보면서 규칙을 공부하는 과정
# predict (예측): 공부한 내용을 바탕으로 실제 시험 문제(x_test)를 푸는 과정
y_pred_linear = svm_linear.predict(x_test)
y_test_arr= y_test.to_numpy()

# # kernel = rbf인 모델
# svm_rbf = SVC(kernel='rbf', C=1.0, gamma=10.0)
# svm_rbf.fit(x_train, y_train)
# y_pred_rbf = svm_rbf.predict(x_test)
#
# # kernel = poly
# svm_sigmoid = SVC(kernel='sigmoid', C=1.0, gamma=10.0)
# svm_sigmoid.fit(x_train, y_train)
# y_pred_sigmoid = svm_sigmoid.predict(x_test)

# confusion matrix 함수
# 예측값과 실제 정답 비교 : y_pred와 y_test를 같은 자료형 nparray로 만들어서 배열 요소를 하나씩 비교함!
def confusionMatrix(pred, test, bool_0):
    tp = tn = fp = fn = 0
    for i in range(len(pred)):
        if pred[i] == test[i]:
            if test[i] == bool_0:
                tp += 1
                # 정답이 1인데 예측도 1로 했을 경우
            else:
                tn += 1
                # 정답이 0인데 예측도 0으로 했을 경우
        else :
            if test[i] == bool_0:
                fn += 1
                # 정답이 1인데 예측을 0으로 했을 경우
            else:
                fp += 1
                # 정답이 0인데 예측을 1로 했을 경우
    return tp, fp, fn, tn

# # confusion matrix 다르게 구현하기!(더 간단하게)
# def confusionMatrix_1(arr1, arr2):
#     tp = tn = fp = fn = 0
#     for i in range(len(arr1)):
#         if arr1[i] == 1 & arr2[i] == 1:
#             tp += 1
#         elif arr1[i] == 0 & arr2[i] == 0:
#             tn += 1
#         elif arr1[i] == 0 & arr2[i] == 1:
#             fp += 1
#         else:
#             fn += 1
#     return tp, tn, fp, fn

# confusion matrix를 이용해서 precision과 recall을 구하는 함수를 만들어야함.
def precision(tp, fp):
    result = tp/(tp+fp)
    return result

def recall(tp, fn):
    result = tp/(tp+fn)
    return result

print("<kernel = linear 이며, 정답값 '0' 기준 결과>")
tp, fp, fn, tn = confusionMatrix(y_pred_linear, y_test_arr, 0)
precision_linear_0 = precision(tp, fp)
recall_linear_0 = recall(tp, fn)
print(f"tp = {tp}, fp = {fp}, fn = {fn}, tn = {tn}")
print("정확도(precision): ", precision_linear_0, "\n재현율(recall): ", recall_linear_0)
print("\n=================================")

print("<kernel = linear 이며, 정답값 '1' 기준 결과>")
tp_1, fp_1, fn_1, tn_1 = confusionMatrix(y_pred_linear, y_test_arr, 1)
precision_linear_1 = precision(tp_1, fp_1)
recall_linear_1 = recall(tp_1, fn_1)
print(f"tp = {tp_1}, fp = {fp_1}, fn = {fn_1}, tn = {tn_1}")
print("정확도(precision): ", precision_linear_1, "\n재현율(recall): ", recall_linear_1)
print("\n=================================")

# print("kernel = RBF 일때 결과")
# mat_rbf = confusionMatrix(y_pred_rbf, y_test_arr)
# precision_rbf = precision(mat_rbf)
# recall_rbf = recall(mat_rbf)
# print(mat_rbf)
# print("정확도(precision): ", precision_rbf, "\n재현율(recall): ", recall_rbf)
#
# print("kernel = sigmoid 일때 결과")
# mat_sigmoid = confusionMatrix(y_pred_sigmoid, y_test_arr)
# precision_sigmoid = precision(mat_sigmoid)
# recall_sigmoid = recall(mat_sigmoid)
# print(mat_sigmoid)
# print("정확도(precision): ", precision_sigmoid, "\n재현율(recall): ", recall_sigmoid)

print("<metrics의 confusion_matrix를 이용한 값 확인>")
from sklearn import metrics
svm_matrix_linear = metrics.confusion_matrix(y_test_arr, y_pred_linear)
print(metrics.classification_report(y_test_arr, y_pred_linear))

