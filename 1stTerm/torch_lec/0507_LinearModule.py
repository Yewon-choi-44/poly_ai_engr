import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# Dataset, Dataloader 사용
from torch.utils.data import Dataset, DataLoader, TensorDataset

# simple data
# 3번의 평가 점수를 통한 최종 성적 예측
# 중간, 기말, 태도
# exam
x_train = torch.FloatTensor([
    [73, 80, 75],
    [90, 85, 95],
    [89,90,95],
    [96, 100, 100]
])
y_train = torch.FloatTensor([
    [152],
    [185],
    [186],
    [198]
])

dataset = TensorDataset(x_train, y_train)

"""
pytorch에서 데이터 셋을 만들어야 데이터 로더 클래스 사용 가능
batch_size는 통상적으로 2의 짐수를 사용 (2, 4, 8, 16 ...)
shuffle은 데이터를 섞어서 가지고 오는 역할 (일반적으로 True로 세팅)


"""

dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# gradient descent 알고리즘 쓴다...
# model = nn.Linear(3, 1)
# optimizer = optim.SGD(model.parameters(), lr=0.01)
model = nn.Linear(3, 1)
optimizer = optim.SGD(model.parameters(), lr=1e-6)

nb_epoch = 5
for epoch in range(nb_epoch+1):
    # for batch_idx, (data, target) in enumerate(dataloader):
    # samples ==data, target
    # 위처럼 저렇게 해도 되고...
    for batch_idx, samples in enumerate(dataloader):
        print(samples)
        x_train, y_train = samples
        # H(x) ==> wx+b (4x3 matmul 3x1 + bias) 해주는 녀석이다 아래는...
        prediction = model(x_train)
        # loss 계산
        loss = F.mse_loss(prediction, y_train)
        optimizer.zero_grad() #누적 미분으로 반드시 해줘야함.
        loss.backward() # w1, w2, w3, b 각각 미분
        optimizer.step() # w1~w3, b 업데이트 (w1 = w1-lr(미분값))
        print(f'Epoch {epoch} | Batch {batch_idx} | Loss {loss.item()}')

# 학습된 결과 확인(파라미터 값 확인)
# 파라미터: w1~w3, b값 뭔지
for param in model.parameters():
    print("-"*30)
    print(param.data) #[w1, w2, w3] ==> b