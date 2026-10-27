import split_dataset
import split_dataset as stt
import pandas as pd
import random
import seaborn as sns
import sklearn.svm as SVC
from sklearn import metrics

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# 데이터 가공-------------------------------------------------------------

# 1. 데이터 split을 함수로 구현 (기존에 랜덤하게 70%는 train, 30%는 test)
# - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할 지 받아서 처리할 것
# 학습 및 평가를 위해 데이터 셋 분리 (과제로도 수행을 했었음)

titanic = sns.load_dataset("titanic")
# print(type(titanic))
# print(titanic.shape)
# print("\n\n",titanic)


titanic = titanic.drop(['alive','embark_town','class','age','deck','adult_male','alone'],axis=1)
titanic['family_size'] = titanic['sibsp']+titanic['parch']
#일단 alone 지움 나중에 살려야하면 살리든지

# sibsp, parch ->> family_size로 합쳤으므로 두 열은 지울거임
titanic = titanic.drop(['sibsp','parch'],axis=1)

#원핫인코딩 (sex, embarked, who)
sex_one_hot = pd.get_dummies(titanic.sex)
embarked_one_hot = pd.get_dummies(titanic.embarked)
who_one_hot = pd.get_dummies(titanic.who)

titanic = pd.concat([titanic, sex_one_hot], axis=1)
titanic = pd.concat([titanic, embarked_one_hot], axis=1)
titanic = pd.concat([titanic, who_one_hot], axis=1)

#원핫인코딩 했으니 sex,embarked, who도 지울거임
titanic = titanic.drop(['sex'], axis=1)
titanic = titanic.drop(['embarked'], axis=1)
titanic = titanic.drop(['who'], axis=1)

idx=stt.shuffleData(titanic)
train_lim, test_lim = stt.cut(idx)
train_X, train_Y, test_X, test_Y = stt.split_train_test(titanic, train_lim, test_lim)




# 2. SVC 커널 변경, C, gamma 값 변경 등을 통해 성능 향상 시키기(2-1, 2-2: mandatory)
# 2-1) 입력 데이터 다양화(예: 성별, who 컬럼 등 포함해서 사용해보기)
# 2-2) svm 파라미터 변경
# 2-3) 그래도 잘 안나온다..==> 구글링 해보시기 바랍니다.
# 2-4) kaggle 순위 높은 방법론들 찾아서 github에서 한 번 확인해보고 정리해보기

# 3. svm_model.predict 결과를 활용하여
# - metrics.confusion_matrix 메서드 직접 구현해보기.
# - metrics.classification_report 메서드 직접 구현.
# 학습된 모델 파라미터로 추론 및 10개 데이터 확인


c = [0.0001,0.001, 0.01, 0.1, 1, 10, 100, 1000]
Gamma = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]

"""
★★★★★★★★★★ 정민님이 알려주심!!!
for c_v C
    for g gamma
        model = SVC(C=c_v, gamma=g)
        model.fit(train_X, train_Y)
        predictions = model.predict(test_X)
        y_true:pd.dataframe, predictions: np.array
        y_true.to_numpy()
        for i len(y_true)
            matrix[y_true[i]][pred[i]] += 1
            [1  0]
            [1  0]
            
        0 tp [0][0]
          tn [1][1]
          fp [0][1]
          fn [1][0]
        1 tp [1][1]
          tn [0][0]
          fp [1][0]
          fn [0][1]
          
precision = tp / (tp + fp)
recall = tp / (tp + fn)
"""

sum_TPN = 0

for i in range(len(c)):
    print()
    for j in range(len(Gamma)):
        svm_model = SVC.SVC(kernel='rbf', C=c[i], gamma=Gamma[j])
        svm_model.fit(train_X, train_Y)
        y_pred = svm_model.predict(test_X)
        svm_matrix = metrics.confusion_matrix(test_Y, y_pred)

        print(f"\nC: {c[i]} | gamma: {Gamma[j]} \n")
        print("==============================")
        print("Confusion Metrics\n", svm_matrix)
        print(f"confusion metrics TN : {svm_matrix[0][0]}")
        print(f"confusion metrics TP : {svm_matrix[1][1]}")
        print(f"confusion metrics sum_TPN : {sum_TPN}")
        print("==============================")
        print("성능 평가 지표\n", metrics.classification_report(test_Y, y_pred))
        print("==============================")

        if (sum_TPN < svm_matrix[0][0] + svm_matrix[1][1]):
            sum_TPN = svm_matrix[0][0] + svm_matrix[1][1]
            winner = metrics.confusion_matrix(test_Y, y_pred)
            winner_report = metrics.classification_report(test_Y, y_pred)
        else:
            continue


print(f"\n젤 좋은 거 설정: {winner} ")
print("\n젤 조은 거 보고서: \n", winner_report)