import torch
import pandas as pd
import numpy
import random
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing()
print(df.feature_names)
print("집값: \n", df.target)
print(len(df.target))
#print(df)
df_tensor = torch.FloatTensor(df.data)

print(type(df_tensor)) #tensor로 변환한 데이터 형 뭐냐
print(type(df_tensor.data)) #뭐가 다르냐
print(df_tensor.data.shape) #numpy type, mxn matrix
#print(df_shuffle[:,:])


#print(df_tensor)
#df_shuffle = torch.randperm(7)
#print("\n",df_shuffle)
#print(len(df_tensor))

# shuffle 수행
df_shuffle_index = torch.randperm(len(df_tensor)) #데이터를 무작위로 섞기
df_shuffle = df_tensor[df_shuffle_index]
df_shuffle_target = df.target[df_shuffle_index]
print("섞은 집값:", df_shuffle_target)

shuffle_len = int(len(df_shuffle.data)*0.7)
print(df.feature_names)
print("\n 섞은 데이터: \n", df_shuffle)
print("\n 썪은데이터몇개: \n", shuffle_len)
print("\n 섞끈데이터몇차원: \n", df_shuffle.data.shape)


train_x = df_shuffle[:shuffle_len, :] #행은 70%까지, 1열부터 8열까지 자름
train_y = df_shuffle_target[: shuffle_len] #70%만 자르되, 8열만 주워갈거다.
print("\n train_x: \n", train_x)
print("\n train_y: \n",train_y)

test_x=df_shuffle[shuffle_len :] # 위에서 70%까지 자른 곳부터 남은 30%를 긁어갈거다.
test_y=df_shuffle_target[shuffle_len:] #남은 30%중 마지막 열에 있는 놈들만 주워갈거다.
print("\n test_x:\n", test_x)
print("\n test_y:\n", test_y)


#3. kfold
shuffle_len_fold = int(len(df_shuffle.data)/5)
print("\n shuffle_len_fold: \n", shuffle_len_fold)

fold_1 = df_shuffle[ : shuffle_len_fold]
fold_2 = df_shuffle[shuffle_len_fold : 2*shuffle_len_fold]
fold_3 = df_shuffle[2*shuffle_len_fold : 3*shuffle_len_fold]
fold_4 = df_shuffle[3*shuffle_len_fold : 4*shuffle_len_fold]
fold_5 = df_shuffle[4*shuffle_len_fold : ]

#avg_fold = (fold_1+fold_2+fold_3+fold_4+fold_5)/5

fold_target_1 = df_shuffle_target[:shuffle_len_fold]
fold_target_2 = df_shuffle_target[shuffle_len_fold+1: 2*shuffle_len_fold]
fold_target_3 = df_shuffle_target[2*shuffle_len_fold: 3*shuffle_len_fold]
fold_target_4 = df_shuffle_target[3*shuffle_len_fold: 4*shuffle_len_fold]
fold_target_5 = df_shuffle_target[4*shuffle_len_fold: 5*shuffle_len_fold]

#avg_fold_target = (fold_target_1+fold_target_2+fold_target_3+fold_target_4+fold_target_5)/5

#print("\n fold_1: \n", fold_1)
#print("\n df_shuffle[0:4129] : \n", df_shuffle[0:4129])
#print("\n fold_2: \n", fold_2)
#print("\n fold_3: \n", fold_3)
#print("\n fold_4: \n", fold_4)
#print("\n fold_5: \n", fold_5)

#print("\n fold_target_1: \n", fold_target_1)
#print("\n fold_target_2: \n", fold_target_2)
#print("\n fold_target_3: \n", fold_target_3)
#print("\n fold_target_4: \n", fold_target_4)
#print("\n fold_target_5: \n", fold_target_5)

train_x_fold_1 = train_x[ : int(len(train_x)/5) ]
train_x_fold_2 = train_x[ int(len(train_x)/5): 2*int(len(train_x)/5)]
train_x_fold_3 = train_x[2*int(len(train_x)/5): 3*int(len(train_x)/5)]
train_x_fold_4 = train_x[3*int(len(train_x)/5): 4*int(len(train_x)/5)]
train_x_fold_5 = train_x[4*int(len(train_x)/5): ]
#avg_trainx_fold = (train_x_fold_1+train_x_fold_2+train_x_fold_3+train_x_fold_4+ train_x_fold_5)/5
#avg_trainx_fold = train_x.mean()
#print(avg_trainx_fold)

train_y_fold_1 = train_y[ : int(len(train_y)/5)]
train_y_fold_2 = train_y[ int(len(train_y)/5): 2*int(len(train_y)/5)]
train_y_fold_3 = train_y[2*int(len(train_y)/5): 3*int(len(train_y)/5)]
train_y_fold_4 = train_y[3*int(len(train_y)/5): 4*int(len(train_y)/5)]
train_y_fold_5 = train_y[4*int(len(train_y)/5): ]
#avg_trainy_fold = (train_y_fold_1+train_y_fold_2+train_y_fold_3+train_y_fold_4+ train_y_fold_5)/5
avg_trainy_fold = train_y.mean()
#print(avg_trainy_fold)

#test_x_fold_1 = test_x[ : int(len(test_x)/5)+1 ]
#test_x_fold_2 = test_x[ int(len(test_x)/5): 2*int(len(test_x)/5) +1]
#test_x_fold_3 = test_x[2*int(len(test_x)/5): 3*int(len(test_x)/5) +1]
#test_x_fold_4 = test_x[3*int(len(test_x)/5): 4*int(len(test_x)/5) +1]
#test_x_fold_5 = test_x[4*int(len(test_x)/5): ]
#avg_testx_fold = (test_x_fold_1+test_x_fold_2+test_x_fold_3+test_x_fold_4+ test_x_fold_5)/5
#avg_testx_fold = test_x.mean()
#print(avg_trainy_fold)

test_y_fold_1 = test_y[ : int(len(test_y)/5)+1 ]
test_y_fold_2 = test_y[ int(len(test_y)/5): 2*int(len(test_y)/5)]
test_y_fold_3 = test_y[2*int(len(test_y)/5): 3*int(len(test_y)/5)]
test_y_fold_4 = test_y[3*int(len(test_y)/5): 4*int(len(test_y)/5)]
test_y_fold_5 = test_y[4*int(len(test_y)/5): ]
#avg_testy_fold = (test_y_fold_1 + test_y_fold_2 + test_y_fold_3 + test_y_fold_4 + test_y_fold_5)/5
avg_testy_fold = test_y.mean()
#print(avg_testy_fold)


n1 = len(test_y_fold_2)+len(test_y_fold_3)+len(test_y_fold_4)+len(test_y_fold_5)
n2 = len(test_y_fold_1)+len(test_y_fold_3)+len(test_y_fold_4)+len(test_y_fold_5)
n3 = len(test_y_fold_1)+len(test_y_fold_2)+len(test_y_fold_4)+len(test_y_fold_5)
n4 = len(test_y_fold_1)+len(test_y_fold_2)+len(test_y_fold_3)+len(test_y_fold_5)
n5 = len(test_y_fold_1)+len(test_y_fold_2)+len(test_y_fold_3)+len(test_y_fold_4)

W = torch.randn(8,1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
#yhat_1 =[]

#yhat_2 =[]
#yhat_3 = []
#yhat_4 = []
#yhat_5 = []

fold_train1= torch.cat([train_x_fold_2,train_x_fold_3,train_x_fold_4,train_x_fold_5],dim=0)
fold_train2= torch.cat([train_x_fold_1,train_x_fold_3,train_x_fold_4,train_x_fold_5],dim=0)
fold_train3= torch.cat([train_x_fold_1, train_x_fold_2, train_x_fold_4, train_x_fold_5],dim=0)
fold_train4= torch.cat([train_x_fold_1, train_x_fold_2, train_x_fold_3, train_x_fold_5],dim=0)
fold_train5= torch.cat([train_x_fold_1, train_x_fold_2, train_x_fold_3, train_x_fold_4],dim=0)

yhat_1= torch.mm(train_x_fold_1, W)+b
yhat_2= torch.mm(train_x_fold_2, W)+b
yhat_3= torch.mm(train_x_fold_3, W)+b
yhat_4= torch.mm(train_x_fold_4, W)+b
yhat_5= torch.mm(train_x_fold_5, W)+b

print("yhat_1: " , yhat_1, yhat_1.size())
print("yhat_2: " , yhat_2, yhat_2.size())
print("yhat_3: " , yhat_3, yhat_3.size())
print("yhat_4: " , yhat_4, yhat_4.size())
print("yhat_5: " , yhat_5, yhat_5.size(), type(yhat_5))

#mse_1 = ((train_y_fold_1 - yhat_1) ** 2).mean()
#print("mse_1: ", mse_1)
sum_1=0
sum_2=0
sum_3=0
sum_4=0
sum_5=0


for i in range(len(yhat_1)):
    sum_1+=(train_y_fold_1[i]-yhat_1[i])**2
    sum_2+=(train_y_fold_2[i]-yhat_2[i])**2
    sum_3+=(train_y_fold_3[i]-yhat_3[i])**2
    sum_4+=(train_y_fold_4[i]-yhat_4[i])**2
    sum_5+=(train_y_fold_5[i]-yhat_5[i])**2
mse_1=(1/len(yhat_1))*sum_1
mse_2=(1/len(yhat_2))*sum_2
mse_3=(1/len(yhat_3))*sum_3
mse_4=(1/len(yhat_4))*sum_4
mse_5=(1/len(yhat_5))*sum_5

print("mse_1: ", mse_1)
print("mse_2: ", mse_2)
print("mse_3: ", mse_3)
print("mse_4: ", mse_4)
print("mse_5: ", mse_5)


RR_1=1-(mse_1/((train_y_fold_1 - train_y_fold_1.mean())**2).mean())
RR_2=1-(mse_2/((train_y_fold_2 - train_y_fold_2.mean())**2).mean())
RR_3=1-(mse_3/((train_y_fold_3 - train_y_fold_3.mean())**2).mean())
RR_4=1-(mse_4/((train_y_fold_4 - train_y_fold_4.mean())**2).mean())
RR_5=1-(mse_5/((train_y_fold_5 - train_y_fold_5.mean())**2).mean())

print("RR_1: ", RR_1)
print("RR_2: ", RR_2)
print("RR_3: ", RR_3)
print("RR_4: ", RR_4)
print("RR_5: ", RR_5)











tx1, tx2, tx3, tx4, tx5 = [torch.FloatTensor(f) for f in
                           [train_x_fold_1, train_x_fold_2, train_x_fold_3, train_x_fold_4, train_x_fold_5]]
# y 데이터들 (반드시 세로 기둥 모양 .view(-1, 1) 로 만들기)
ty1, ty2, ty3, ty4, ty5 = [torch.FloatTensor(f).view(-1, 1) for f in
                           [train_y_fold_1, train_y_fold_2, train_y_fold_3, train_y_fold_4, train_y_fold_5]]

# 2. 훈련용 데이터 합치기 (질문자님이 짠 로직 그대로)
# 예시로 1번 폴드를 시험지로 쓰고, 2~5번을 합쳐서 공부용으로 씀
fold_train_x = torch.cat([tx2, tx3, tx4, tx5], dim=0)
fold_train_y = torch.cat([ty2, ty3, ty4, ty5], dim=0)

# 3. 모델 파라미터 초기화
W = torch.randn(8, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
lr = 0.0000001  # 숫자가 nan으로 나오면 0을 하나 더 붙이세요

print("--- 학습 시작 ---")

# 4. 학습 루프 (100번 반복)
for epoch in range(1000):
    # 예측 및 오차 계산
    yhat = torch.mm(fold_train_x, W) + b
    loss = ((fold_train_y - yhat) ** 2).mean()

    # 역전파 및 가중치 업데이트
    loss.backward()
    with torch.no_grad():
        W -= W.grad * lr
        b -= b.grad * lr
        W.grad.zero_()
        b.grad.zero_()

    if (epoch + 1) % 20 == 0:
        print(f"에폭 [{epoch + 1}/100] MSE: {loss.item():.4f}")

# 5. 검증 (숨겨놨던 1번 폴드로 시험 보기)
with torch.no_grad():
    yhat_test = torch.mm(tx1, W) + b
    mse_test = ((ty1 - yhat_test) ** 2).mean()

    # 결정계수(R2) 계산
    y_bar = ty1.mean()
    denominator = ((ty1 - y_bar) ** 2).mean()
    r2_score = 1 - (mse_test / denominator)

print("-" * 30)
print(f"1번 폴드 최종 MSE: {mse_test.item():.4f}")
print(f"1번 폴드 최종 R2: {r2_score.item():.4f}")





























'''
print(f"avg_trainx_fold: {avg_trainx_fold}")
print(f"avg_train_x_fold_1: {train_x_fold_1.mean()}")
print(f"avg_train_x_fold_2: {train_x_fold_2.mean()}")
print(f"avg_train_x_fold_3: {train_x_fold_3.mean()}")
print(f"avg_train_x_fold_4: {train_x_fold_4.mean()}")
print(f"avg_train_x_fold_5: {train_x_fold_5.mean()}\n")

print(f"avg_trainy_fold: {avg_trainy_fold.mean()}")
print(f"avg_train_y_fold_1: {train_y_fold_1.mean()}")
print(f"avg_train_y_fold_2: {train_y_fold_2.mean()}")
print(f"avg_train_y_fold_3: {train_y_fold_3.mean()}")
print(f"avg_train_y_fold_4: {train_y_fold_4.mean()}")
print(f"avg_train_y_fold_5: {train_y_fold_5.mean()}\n")

print(f"avg_testx_fold: {avg_testx_fold.mean()}")
print(f"avg_test_x_fold_1: {test_x_fold_1.mean()}")
print(f"avg_test_x_fold_2: {test_x_fold_2.mean()}")
print(f"avg_test_x_fold_3: {test_x_fold_3.mean()}")
print(f"avg_test_x_fold_4: {test_x_fold_4.mean()}")
print(f"avg_test_x_fold_5: {test_x_fold_5.mean()}\n")

print(f"avg_testy_fold: {avg_testy_fold.mean()}")
print(f"avg_test_y_fold_1: {test_y_fold_1.mean()}")
print(f"avg_test_y_fold_2: {test_y_fold_2.mean()}")
print(f"avg_test_y_fold_3: {test_y_fold_3.mean()}")
print(f"avg_test_y_fold_4: {test_y_fold_4.mean()}")
print(f"avg_test_y_fold_5: {test_y_fold_5.mean()}\n")
'''

