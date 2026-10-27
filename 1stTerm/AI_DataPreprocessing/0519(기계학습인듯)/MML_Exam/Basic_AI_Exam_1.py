import seaborn as sns
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import torch.nn.functional as F
import pandas as pd
import sklearn.svm as SVC
from sklearn import metrics


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


# 데이터셋 로드
titanic = sns.load_dataset("titanic")
print()

print(titanic.head())
print(titanic.info())
# 필요없는 열 탈락
titanic = titanic.drop(["class", "embark_town", "fare", "deck", "alive", "adult_male","age"], axis=1)

titanic['family_size'] = titanic['sibsp']+titanic['parch']
titanic = titanic.drop(['sibsp','parch'], axis=1)

titanic['embarked'].fillna('C')
print(titanic.info())

#원핫인코딩

sex_dum = pd.get_dummies(titanic.sex)
embarked_dum = pd.get_dummies(titanic.embarked)
who_dum = pd.get_dummies(titanic.who)

cat = [sex_dum, embarked_dum, who_dum]

for i in cat:
    titanic = pd.concat([titanic,i],axis=1)



titanic = titanic.drop(['sex'], axis=1)
titanic = titanic.drop(['embarked'], axis=1)
titanic = titanic.drop(['who'], axis=1)

# 타겟과 feature 분리
X = titanic.drop("survived", axis=1)
print(X.head())
y = titanic["survived"]
print(y.head())


scaler = StandardScaler()
#
# transformed_y = scaler.transform(y)

# transformed_y = torch.tensor(transformed_y)
#
print(titanic.info())
# print("X.info()\n",X.info())
# print("y.info()\n",y.info())
# print(transformed_X.shape)
# print(y.shape)



#훈련 데이터와 테스트 데이터 분리
c = [0.0001,0.001, 0.01, 0.1, 1, 10, 100, 1000]
Gamma = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

sum_TPN = 0

for i in range(len(c)):
    print()
    for j in range(len(Gamma)):
        svm_model = SVC.SVC(kernel='rbf', C=c[i], gamma=Gamma[j])
        svm_model.fit(X_train, y_train)
        y_pred = svm_model.predict(X_test)
        svm_matrix = metrics.confusion_matrix(y_test, y_pred)

        print(f"\nC: {c[i]} | gamma: {Gamma[j]} \n")
        print("==============================")
        print("Confusion Metrics\n", svm_matrix)
        print(f"confusion metrics TN : {svm_matrix[0][0]}")
        print(f"confusion metrics TP : {svm_matrix[1][1]}")
        print(f"confusion metrics sum_TPN : {sum_TPN}")
        print("==============================")
        print("성능 평가 지표\n", metrics.classification_report(y_test, y_pred))
        print("==============================")

        if (sum_TPN < svm_matrix[0][0] + svm_matrix[1][1]):
            sum_TPN = svm_matrix[0][0] + svm_matrix[1][1]
            winner = metrics.confusion_matrix(y_test, y_pred)
            winner_report = metrics.classification_report(y_test, y_pred)
        else:
            continue


print(f"\n젤 좋은 거 설정: {winner} ")
print("\n젤 조은 거 보고서: \n", winner_report)

# accuracy = winner_report[2][2]

# print(f"Accuracy: {accuracy:.4f}")
exit()



#2. 모델 성능 향상 해보기.

svm_model = SVC.SVC(kernel='rbf',C=0.1, gamma=10.0)
svm_model.fit(train_X_encoded, train_Y)
print(svm_model.score(train_X_encoded, train_Y))

#sex열 원핫인코딩
train_X_encoded = pd.get_dummies(train_X, columns=['sex','alive'])
print(train_X_encoded)



exit()
# 표준화

scaler.fit(X_train)
# transformed_X = torch.tensor(X_train)
X_train = scaler.transform(X_train)

# transformed_X = torch.tensor(X_train)
X_train = torch.tensor(X_train)
# y_train = torch.tensor(y_train)


w = torch.zeros((2,1), requires_grad = True)
b = torch.zeros(1, requires_grad = True)

#모델 생성
# model = nn.Sequential(nn.Linear(X_train.shape[1], 100),
#                       nn.Sigmoid())
optimizer = optim.SGD([w,b], lr=1e-6)


nb_epoch = 10
for epoch in range(nb_epoch):
    temp_x = X_train.matmul(w) + b
    hx =  1 / (1 + torch.exp(-temp_x))
    loss = F.binary_cross_entropy(hx, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 1 == 0:
        print(f"epoch {epoch}, loss {loss}")

print(w, b)
prediction = torch.sigmoid(X_train.matmul(w)+b)
print(prediction)


pred = []
for i in list(prediction):
    if i > 0.5: pred.append(1)
    else:
        pred.append(0)
print(pred)

result = prediction >= torch.FloatTensor([0.5])
print(result)







# model = train_test_split(X_train, y_train, test_size = 0.2, random_state = 42)
# optimizer = optim.Adam(model.parameters())






#