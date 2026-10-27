import torch
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
from Own_ML_Class import BinaryClassification

# x_data: 6x2 짜리
# y_data: 6x1 짜리
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0],[0],[0],[1],[1],[1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# nn.sequenital() : nn.Module 층을 차례로 쌓을 수 있도록 ㅎ하는 것
# keras (tensorflow) 유사하게 사용, 딥러닝 층을 여러층을 쌓기 때문에 sequential 내에 layer 층 쌓음
# 쉽게 여러 함수들을 연결시켜주는 기능.

model = nn.Sequential(nn.Linear(2, 1),
                      nn.Sigmoid())

# model.parameters(): ?? 2x1: w, 1: b
optimizer = optim.SGD(model.parameters(), lr=1)
# for params in model.parameters():
#     print(params) # 초기 모델 파라미터 값 확인

nb_epoch = 3000
for epoch in range(nb_epoch+1):
    hx = model(x_train)
    loss = F.binary_cross_entropy(hx, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'epoch: {epoch}, loss: {loss}')