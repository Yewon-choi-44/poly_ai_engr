import torch
import random
import sklearn.datasets
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing()
df_tensor = torch.FloatTensor(df.data)
print(df)
print()
print(df_tensor)
print()