import torch
import seaborn as sns
import pandas as pd
sea = sns.load_dataset("titanic")
print(sea.head())

sea_tensor = torch.Tensor(sea)
print(sea_tensor)