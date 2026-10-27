 from sklearn import metrics
from sklearn.svm import SVC # 모델선정
import pandas as pd
import seaborn as sns
import split_dataset as sd

pd.set_option('display.max_columns', None) #none을 입력하여 데이터 전체를 확인.
t_data = sns.load_dataset('titanic') # 반환되는 타입이 판다스이기 때문에 그대로 사용.
# print(t_data)
# print(t_data.head()) # 데이터셋의 속성 확인.
# print(t_data.info()) # 데이터셋의 정보 확인.
#---------------------------------------------------------

# <<누락데이터 및 누락수>>
# age: 177, embarked: 2, deck : 688 /

# <<숫자형이 아닌 데이터(SVM은 숫자형 데이터만 받을 수 있다.)>>
# sex, embarked, who, deck, embark_town, alive

# <<중복되는 데이터>>
# pclass(중복, int) = calss(중복, str), embarked_town(중복, str) = embarked(중복, str),
# alive(중복, str) = survied(중복, int)

# <<드롭 데이터 결정(결정사유)>>
# age(누락), deck(누락), class(중복, str), embark_town(중복, str), alive(중복, str)

# <<형 변환 필요 데이터 선정>>
# sex, embarked, who

#---------------------------------------------------------
# <<누락 및 동일 데이터 드롭>>
df = t_data.drop(['age', 'deck', 'class', 'embark_town', 'alive'], axis = 1)
# print(df.info())
#print(df['embarked'])

#-----------------------
#<<누락 데이터 보완>>

#<<df의 embarked 속성 중 null데이터 확인>>
# print(df[df['embarked'].isnull()])
# 61행, 829행 null

#-----------------------
# <<최빈도 확인을 위해 데이터 종류 및 빈도 확인>>

# <<데이터 종류확인>>
#sd.listdataCheck(df['embarked'])
# 데이터 종류는 ['S', 'C', 'Q'] 3가지로 확인

#-----------------------
# <<데이터 빈도 확인>>
#print(len(df[df['embarked'] == 'S'])) # 644 / 최빈도 데이터이므로 61, 829행에 기입
#print(len(df[df['embarked'] == 'C'])) # 168
#print(len(df[df['embarked'] == 'Q'])) # 77

#-----------------------
# <<데이터 기입>>
df.loc[[61, 829], 'embarked'] = 'S' # 데이터 기입
#print(df[df['embarked'].isnull()]) # 기입 여부 확인

#---------------------------------------------------------
#<<분류기(SVM)가 읽을 수 있는 데이터 형변환>>
#<<형 변환 필요 데이터>>
# embarked(one_hot encoding), sex(int 변환 예정), who(int 변환 예정)

#-----------------------
#<<embarked 데이터 one-hot encoding 및 데이터 셋 삭제 및 추가>>
one_hot_embarked = pd.get_dummies(df.embarked) #one-hot encoding
df.drop(['embarked'], axis = 1, inplace = True) #기존 데이터 삭제
df = pd.concat([df,one_hot_embarked], axis=1) # one-hot encoding 데이터추가

#-----------------------
#<sex의 자료 종류 확인 및 데이터 형 변환>
#sd.listdataCheck(df['sex']) # 자료형 male, female
sex_int = []
for i in range(len(df['sex'])):
    if df['sex'][i] == "male":
        sex_int.append(0)
    else:
        sex_int.append(1) # 자료형 변경

sex_int = pd.DataFrame(sex_int, columns= ['sex_int']) #리스트를 데이터프레임으로 변경 및 속성명 기입
df.drop(['sex'], axis = 1, inplace=True) # 기존 sex데이터 삭제
df = pd.concat([df,sex_int], axis=1) # sex_int데이터 추가
#-----------------------
#<who의 자료 종류 확인 및 데이터 형 변환>
#sd.listdataCheck(df['who']) # 자료형 man, woman, child

who_int = []
for i in range(len(df['who'])):
    if df['who'][i] == "man":
        who_int.append(0)
    elif df['who'][i] == "man":
        who_int.append(1)
    else:
        who_int.append(2) # 자료형 변경

who_int = pd.DataFrame(who_int, columns= ['who_int']) #리스트를 데이터프레임으로 변경 및 속성명 기입
df.drop(['who'], axis = 1, inplace=True) # 기존 who데이터 삭제
df = pd.concat([df,who_int], axis=1) # who_int데이터 추r가
#print(df.info())
#print(df)
#---------------------------------------------------------
# <<데이터셋 분리 함수를 만들고 만든 함수를 이용해 데이터셋 분리>>

# <<학습 데이터 준비>>
x = df.loc[:, 'pclass':'who_int']
y = df['survived']

#-----------------------

# <<만든함수로 데이터셋 분리>>
x_train, x_test, y_train, y_test = sd.split_train_test(x, y, 0.3)
# print(len(x_train))
# print(len(x_test))
# print(len(y_train))
# print(len(y_test))

#---------------------------------------------------------
# <<모델 선정 및 파라미터 셋팅>>

# kenel = rbf(가우시안 커널: Radial Basis Function)
# - 가장 일반적인 커널로 데이터 포인터 간의 거리를 기준으로 무한 차원까지 매핑하여
# 매우 복잡한 비선형 데이터도 분류할 수 있다.
#
# c = 규제 파라미터: 오분류에 대한 허용오차를 조절한다. >> 오분류를 얼마나 엄격하게 제한할 것인가.
# - 값이 크면 오차를 허용하지 않으려 하고 이에 따라 결정 경계가 복잡해지며 과대적합 위험 증가
# - 값이 작으면 오차를 많이 허용하여 경계선이 직선에 가까워지며 과소적합 위험 증가
#
# gamma = 커널 계수: 데이터 포인트가 영향을 미치는 거리 결정 >> 하나의 서포트 벡터가 미치는 영향력이 얼마나 멀리 있는가?
# - 값이 크면 영향력이 미치는 거리가 짧아짐.
# 서포트 벡터가 매우 국지적으로 작용하여 결정 경계가 굴곡진 형태가 되어 과대 적합 위험
# - 값이 작으면 영향력이 미치는 거리가 길어짐.
# 결정 경계가 부드러워지고 완만해져 과소 적합 위험
#
# 1. 과대적합(overfitting) : 모델이 학습 데이터를 너무 '외워버려서' 처음 보는 데이터에 대한 일반화 능력이 부족해진 상태
# - 훈련 데이터 정확도 매우 높음
# - 검증 / 테스트 데이터 정확도 낮음
# 오차: 학습 데이터에 대한 손실은 낮지만, 검증 데이터 손실은 높음.
#
# 2. 과소적합(underfitting): 모델이 너무 단순하여 훈련 데이터의 내재된 구조조차 학습하지 못해 학습 데이터와
# 새로운 데이터 모두에서 낮은 성능을 보이는 현상입니다.
# - 훈련 데이터 정확도 낮음
# - 검증/테스트 데이터 정확도 낮음
# 오차: 학습 데이터와  검증 데이터 모두에서 오차가 높음


# 모델 선정 및 파라미터 셋팅
svm_model = SVC(kernel ='rbf', C=10, gamma=0.001)
#-----------------------

# 인공지능 모델 학습
svm_model.fit(x_train, y_train)

#-----------------------

#학습된 모델 파라미터로 새로운 데이터를 이용한 추론 결과를 변수에 대입
y_pred = svm_model.predict(x_test)

#-----------------------

#metrics.confusion: confusion matrix를 구하는 행
svm_matrix = metrics.confusion_matrix(y_test, y_pred)
print(svm_matrix)


print(metrics.classification_report(y_test, y_pred))
# metrics.classification_report : precision, recall, f1 지표 확인 가능 / metrics:성능평가 기준
print()
#from sklearn.model_selection import GridSearchCV: 결과값에 대해 가장 신뢰되는 결과를 선정해주는 함수


#---------------------------------------------------------

#<<성능 평가 지표 직접구현>>

#<Confusion Matrix 직접 구현>
# y_test는 실제값 / y_pred는 예측값
tn = 0 # 실제값이 0(사망)일 때 예측값도 0(사망)인것
fn = 0 # 실제값이 0(사망)일 때 예측값이 1(생존)인것
tp = 0 # 실제값이 1(생존)일 때 예측값이 1(생존)인것
fp = 0 # 실제값이 1(생존)일 때 예측값이 0(사망)인것
y_test = list(y_test)
for i in range(len(y_test)):
    if y_test[i] == 0:
        if y_test[i] == y_pred[i]:
            tn += 1 # 실제값이 0이고 예측값도 0일 때 1일씩 올라감
        else:
            fn += 1 # 실제값이 0이고 예측값도 1일 때 1일씩 올라감
    elif y_test[i] == 1:
        if y_test[i] == y_pred[i]:
            tp += 1 # 실제값이 1이고 예측값도 1일 때 1일씩 올라감
        else:
            fp += 1 # 실제값이 1이고 예측값도 0일 때 1일씩 올라감

#<Confution Mtrix 구현결과>
confusionlist = [
    [tn, fp],
    [fn, tp]
]
print(f'cofusion_matrix: {confusionlist}')

#-----------------------

# <precision, recall 구현>
precision_0 = (tn/(tn+fn)) #precision: 예측값 사망(0)을 기준으로 실제값도 사망(0)인 비율
recall_0 = (tn/(tn+fp)) # recall: 실제값 사망(0)을 기준으로 예측값이 사망(0)인 비율
precision_1 = (tp/(tp+fp)) #precisionr 1이 기준일 때: 예측값 생존(1)을 기준으로 실제값도 생존(1)인 비율
recall_1 = (tp/(tp+fn)) # recall 1이 기준일 때: 실제값 생존(1)을 기준으로 예측값이 생존(1)인 비율

print(f'precision_0: {precision_0:.2f}')
print(f'recall_0: {recall_0:.2f}')
print(f'precision_1: {precision_1:.2f}')
print(f'recall_1: {recall_1:.2f}')
#---------------------------------------------------------