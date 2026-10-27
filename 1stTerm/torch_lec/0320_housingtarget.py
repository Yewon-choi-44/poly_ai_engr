import numpy as np
import pandas as pd
import torch
import random
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
#print(housing)


#print(type(housing))
#print(type(housing.data))
#print(housing.data.shape) #numpy type, mxn matrix
cal_tensor = torch.FloatTensor(housing.data)


#전체 데이터의 70%를 학습 데이터 셋으로 활용하고
#30%를 테스트 데이터셋으로 구성하여 평가를 진행하고자 한다.
#위 내용을 반영하여 데이터셋을 구축을 하세요.

train_len = int(len(housing.data) * 0.7)
print(train_len)

train_x=cal_tensor[:train_len, :7]
train_y = cal_tensor[0 : train_len: 7] #0번째 행부터  train_len - 1번째 행까지 (==> random하게 70%가지고 오는 것)
print("\n train_x: \n", train_x)
print("\n train_y: \n",train_y)


test_x=cal_tensor[train_len: , :7]
test_y=cal_tensor[train_len: , 7]
print("\n test_x:\n", test_x)

print(train_x.shape,train_y.shape)
print(test_x.shape,test_y.shape)

rand_list=[1,3,7] #중복되지 않은 행을 랜덤하게 가지고 왔어요...
train_x_rand = cal_tensor[rand_list, :7]

print(train_x_rand.shape)
print(train_x_rand)