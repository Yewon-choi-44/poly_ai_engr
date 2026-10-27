#데이터를 가지고 와서 텐서 타입으로 만들어 둔 것.
import numpy as np
import pandas as pd
import torch
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
#print(housing)




#print(type(housing))
#print(type(housing.data))
#print(housing.data.shape) #numpy type, mxn matrix
#cal_tensor = torch.FloatTensor(housing.data)
##cal_tensor = torch.from_numpy(cal_tensor)
#print(cal_tensor.size())
#print(cal_tensor.dim())
#print(cal_tensor[:10,:])


#전체 데이터의 70%를 학습 데이터 셋으로 활용하고
#30%를 테스트 데이터셋으로 구성하여 평가를 진행하고자 한다.
#위 내용을 반영하여 데이터셋을 구축을 하세요.

train_len = int(len(housing.data) * 0.7)
print(train_len)