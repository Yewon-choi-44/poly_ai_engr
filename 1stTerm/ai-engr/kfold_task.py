import torch
import random
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing()
#print(df)
df_tensor = torch.FloatTensor(df.data)
#print(df_tensor)


df_shuffle = torch.randperm(7)
print("\n",df_shuffle)