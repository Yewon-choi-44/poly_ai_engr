'''import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import torchvision.datasets as dsets            # mnist, fashin mnist 등 가지고 올 수 있음
import torchvision.transforms as transforms     # dataset --> Tensor로 변경, to Image 이미지로 변경을 하거나... 그런 기능들이 있음
                                                # dataset이 다운을 받으면 g?z?파일로 존재를 하는데 그거를 텐서나 이미지로 변환을 해줌...
import time
zoo_df = pd.read_csv("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0519(기계학습인듯)/data/data-04-zoo.csv")
data_loader = torch.utils.data.DataLoader(zoo_df, batch_size=256, shuffle=True)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
# f_zoo_train = dsets.Fa(root='./data', train=True,
#                           transform=transforms.ToTensor(), download=True)
#
# mnist_train = dsets.MNIST(root='./data', train=True,
#                           transform=transforms.ToTensor(), download=True)
# mnist_test = dsets.MNIST(root='./data', train=False,
                         transform=transforms.ToTensor(), download=True)

#Dataloader
data_loader = torch.utils.data.DataLoader(mnist_train,
                                          batch_size=256, shuffle=True) #찾아보기. 배치사이즈 크게 잡을수록 속도는 빠르다.
transform = transforms.ToPILImage()

###################################################################################
# 여기는 fashion_MNIST 임. -> 옷 들어있는 데이터셋임 부츠랑... 이것저것
print(f_mnist_train)
for i in range(20,40):
    img = transform(f_mnist_train[i][0])
    print(f_mnist_train[i][1])
    print(img.size)
    plt.imshow(img, cmap='gray')
    plt.show()
exit()
'''
##############################################################################
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 각 샘플은 4개의 특성을 가지고 있으며, 8개의 샘플이 존재
# 8x4



zoo_df = pd.read_csv("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0519(기계학습인듯)/data/data-04-zoo.csv")
zoo_df= zoo_df.drop(zoo_df.index[:],axis=0)
# print(type(zoo_df))
zoo_df = zoo_df.reset_index(drop=True)
# print(zoo_df)
zoo_df = zoo_df.apply(pd.to_numeric, errors='coerce').fillna(0)

x_train = torch.FloatTensor(zoo_df.values.astype(float))

##############################################
num_features = x_train.shape[1]  # 자동으로 17이 할당됩니다.
num_classes = 7
w = torch.randn((num_features,num_classes), requires_grad=True)
b = torch.randn(num_classes, requires_grad = True)
# optimizer = optim.SGD([w,b], lr=0.01)
optimizer = optim.Adam([w,b], lr=0.01)

nb_epoch = 1000
for epoch in range(nb_epoch+1):
    # hx = F.softmax(x_train.matmul(w) + b, dim=1)
    # 선형 회귀 결과 계산
    z = x_train.matmul(w)+b
    hx = F.softmax(z, dim=1)

    # 파이토치 표준 다중 클래스 분류 손실 함수 사용 (z값과 실제 정답 y_train 비교)
    # loss = F.cross_entropy(z, y_ytai
    loss = (hx * -torch.log(hx + 1e-5)).sum(dim=1).mean()


    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss {loss.item():.4f}')
exit()


# 2 이면...
# [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]
# one-hot encoding으로 변경(8)
# unsqueeze(0) --> 1x8
# unsqueeze(1) --> 8x1
# 0은 항상 row 단위, 1은 항상 column 단위

x_train = torch.FloatTensor(x_train)

# y_onehot = torch.FloatTensor(x_train)
# one-hot encoding: F.onehot, pd.dummies, 직접 가공...
# 내가 코드를 만들면 F.onehot 사용...
# github에 프로젝트를 많이 참고 하게 됨...

# y_onehot = torch.zeros(8, 3)
# y_onehot = y_onehot.scatter(1, y_train.unsqueeze(1), 1)
y_train = torch.LongTensor(y_train)
y_onehot = F.one_hot(y_train, 3)
print(x_train.shape)
print(y_onehot)

############################
# 모델 파라미터 초기화 (w, b)
# softmax(wx+b) ==> softmax(x_train.matmul(w) + b)
w = torch.zeros((4, 3), requires_grad=True)
b = torch.zeros(1, requires_grad=True) #1: broadcast 방식으로 다 더해짐 3: 각각의 bias 존재
optimizer = optim.SGD([w, b], lr=0.01)
# optimizer = optim.Adam([w, b], lr=0.01) # 이거 써도 문제는 없다고 하심...
                                          # 최근에는 Adam을 더 많이 쓰기도 한다고 하심
                                          # Adam(무지성으로 그냥 많이 지정해서 사용)
                                          # SGD(특정한 목적이 아니면 학습용도로 많이 사용!)

nb_epoch = 1000
for epoch in range(nb_epoch+1):
    hx = F.softmax(x_train.matmul(w) + b, dim=1)
    loss = (y_onehot * -torch.log(hx)).mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch {epoch}: Loss {loss.item():.4f}')
