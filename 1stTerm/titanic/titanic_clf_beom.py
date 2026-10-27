import pandas as pd
import seaborn as sns
from sklearn.svm import SVC
from sklearn import metrics
from split_dataset import split_train_test


pd.set_option('display.max_columns', None)
t_data = sns.load_dataset('titanic')

# print(t_data.head())

# pclass_one_hot = pd.get_dummies(t_data['pclass'])
# print(pclass_one_hot.head())

# Boolean Indexing
# df_1 = t_data[t_data['survived'] == 0]
# df_2 = t_data[t_data['survived'] == 1]
# df_3 = t_data[(t_data['survived'] == 1) & (t_data['age'] >= 30)]

# df.drop(['sex', 'who', 'embarked'], axis = 1, inplace = True)

# print(len(df_1), len(df_2), len(df_3))

df = t_data.drop (['deck' , 'age' , 'alive', 'class', 'embark_town'], axis = 1)
# print(df.head)
# exit()

# one-hot-encording

pclass_one_hot = pd.get_dummies(t_data['pclass'], prefix = 'pclass')
sex_one_hot = pd.get_dummies(t_data['sex'], prefix = 'sex')
who_one_hot = pd.get_dummies(t_data['who'], prefix = 'who')

# print(pclass_one_hot.head())
# print(sex_one_hot.head())
# print(who_one_hot.head())
# print(df1)
embarked_one_hot = pd.get_dummies(t_data['embarked'], prefix = 'embarked')


# df1 = t_data['who_int'] = t_data['who'].map({'man': 0, 'woman': 1, 'child': 2})
# 삭제할 열 리스트 (글자로 된 열, 중복된 열, 분석에 필요 없는 열 등)
# cols_to_drop = ['pclass', 'sex', 'embarked', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'class', 'survived']
df1 = pd.concat([t_data, pclass_one_hot, sex_one_hot, who_one_hot, embarked_one_hot], axis = 1)
df1.loc[[61, 829], 'embarked'] = 's'
df1 = df1.drop( ['pclass', 'sex', 'embarked', 'who'], axis = 1)
df1 = df1.drop (['deck' , 'age' , 'alive', 'class', 'embark_town', 'adult_male', 'fare'], axis = 1)
# print(df1.head())
# df1.to_excel('AI_ML_HW4.xlsx', index = False)

# 데이터 정리
# df_train = df1.drop(cols_to_drop, axis=1)
#
# print(df_train.head())
# print(df_train.info())


# df1 = df.drop(['deck', 'age', 'alive', 'embark_town', 'class'], axis = 1)

# for idx, val in df['who'] :
#     if val == 'men' : df['who_int'] = 0
#     if val == 'women' : df['who_int'] = 1
#     if val == 'child' : df['who_int'] = 2

# print(df1['who_int'])

# print(embarked_one_hot.head())


# 1.     학습 데이터 준비 - > 지도학습으로 생존여부를 판단하고자 함.

# x = df_train.drop('pclass', axis = 1)
# y = df_train['pclass']

# x_tensor = df1.loc[:, 'sibsp' : 'embarked_3']
# y_tensor = df1['survived']
x_tensor = df1.drop('survived', axis = 1)
y_tensor = df1['survived']

# 과제 1. 데이터 split을 함수로 구현 (기존에 랜덤하게 70% 는 train, 30%는 test split set을 구축했음)
#  - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할 지 받아서 처리할 것.

x_train, y_train, x_test, y_test = split_train_test(x_tensor, y_tensor)

# print(x_train.head())
# # print(y_train.head())
# print(x_train,'*********************', x_test,'*********************', y_train,'*********************' ,y_test)
# x_train = df.loc[:, 'pclass' : 'alone']
# y_train = df['survived']
# x_test = df.loc[:, 'pclass' : 'alone']
# y_test = df['survived']

# 2.    모델 선정 및 파라미터 세팅
svm_model = SVC(kernel = 'rbf', C = 10, gamma = 0.01)
svm_model.fit(x_train, y_train)

# 2 - 1     학습된 모델 파라미터로 추론 및 10개 데이터 잘 되는지 확인.
y_pred = svm_model.predict(x_test)
# print(y_pred[0:10])
# print(y_test[0:10])

# 3.    svm_matrix 결과값 만들어서 출력하기.

# actual = y_test
# predicted = y_pred

# TP = 0
# FP = 0
# TN = 0
# FN = 0
#
# for 문으로 만들었던 confusion Matrix. (Positive 값이 0일때를 찾을수 없어서 폐기)
# for a, p in zip(actual, predicted) :
#     if a == 1 and p == 1 :
#         TP += 1
#     elif a == 0 and p == 1 :
#         FP += 1
#     elif a == 0 and p == 0 :
#         TN += 1
#     elif a == 1 and p == 0 :
#         FN += 1

def confusionMat(pred, test, rage_0):
    TP = FP = TN = FN = 0
    for i in range(len(pred)) :
        if pred[i] == test.iloc[i] :
            if test.iloc[i] == rage_0 :
                TP += 1
            else :
                TN += 1
        else :
            if test.iloc[i] == rage_0 :
                FN += 1
            else :
                FP += 1
    return TP, FP, TN, FN


def prediction (TP, FP) :
    result = TP / (TP + FP)
    return result

def recall (TP, FN) :
    result = TP / (TP + FN)
    return result


print('kernel = ref, Positive 가 0 일때의 결과값')
TP, FP, TN, FN = confusionMat(y_pred, y_test, 0)
pre_0 = prediction(TP, FP)
rec_0 = recall (TP, FN)

print(f'TP : {TP}, FP : {FP}, TN : {TN}, FN : {FN} 이며, ')
print(f'Prediction(정확도) :  {pre_0:.4f}, \t 이며 Recall(재현율) : {rec_0:.4f}')
print('-----------------------------------------------------------------------------------')

print('kernel = ref, Positive 가 1 일때의 결과값')

TP_1, FP_1, TN_1, FN_1 = confusionMat(y_pred, y_test, 1)
pre_1 = prediction(TP_1, FP_1)
rec_1 = recall(TP_1, FN_1)

print(f'TP : {TP_1}, FP : {FP_1}, TN : {TN_1}, FN : {FN_1} 이며, ')
print(f'Prediction(정확도) : {pre_1:.4f}, \t 이며 Recall(재현율) : {rec_1:.4f}')
print('-----------------------------------------------------------------------------------')

# print(f'prediction (정밀도) : {prediction:.4f}')
# print(f'recall (재현율) : {recall:.4f}')

print('참고용 데이터 확인자료.')

svm_matrix = metrics.confusion_matrix(y_test, y_pred)
print(f'svm : {svm_matrix}')
print(metrics.classification_report(y_test, y_pred))

print('-----------------------------------------------------------------------------------')
