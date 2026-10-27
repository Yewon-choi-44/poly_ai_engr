import torch
import pandas as pd
import numpy
import random
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing()
print(df.feature_names)
print("집값: \n", df.target)
print(len(df.target))
df_tensor = torch.FloatTensor(df.data)

print(type(df_tensor)) 
print(type(df_tensor.data)) 
print(df_tensor.data.shape) 


# shuffle 수행
df_shuffle_index = torch.randperm(len(df_tensor)) #데이터를 무작위로 섞기
df_shuffle = df_tensor[df_shuffle_index]
df_shuffle_target = df.target[df_shuffle_index]

shuffle_len = int(len(df_shuffle.data)*0.7)
print(df.feature_names)

train_x = df_shuffle[:shuffle_len, :] 
train_y = df_shuffle_target[: shuffle_len] 

test_x=df_shuffle[shuffle_len :] 
test_y=df_shuffle_target[shuffle_len:] 