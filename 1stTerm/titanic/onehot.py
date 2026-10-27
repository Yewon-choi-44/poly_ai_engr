import pandas as pd
data_dic = {'label':['Apple', 'Samsung', 'LG', 'Samsung']}
df = pd.DataFrame(data_dic)

pd_oh_encoded = pd.get_dummies(df['label'])
print(pd_oh_encoded)