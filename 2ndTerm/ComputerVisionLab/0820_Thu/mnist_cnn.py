# mnist_cnn.py

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import torchvision.datasets as dsets            # mnist, fashion mnist 등 가지고 올 수 있음
import torchvision.transforms as transforms 
import time
from Own_ML_Class import CNN


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
mnist_train = dsets.MNIST(root='./data', train=True,
                          transform=transforms.ToTensor(), download=True)

mnist_test = dsets.MNIST(root='./data', train=False,
                         transform=transforms.ToTensor(), download=True)

#Dataloader
data_loader = torch.utils.data.DataLoader(mnist_train,
                                          batch_size=100, shuffle=True) # 찾아보기. 배치사이즈 크게 잡을수록 속도는 빠르다.

##################################################################################

#CNN 모델 정의
model = CNN().to(device)
loss_fn = nn.CrossEntropyLoss() # softmax(wx+b)
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(4):
    # batch_size=100, training dataset : 50000
    # iter : 50000/100 -> 500 --> 500번을 돌아야 1epoch
    
    avg_loss = 0

    for X, Y in data_loader:
        X = X.to(device)
        Y = Y.to(device)

        optimizer.zero_grad()
        Y_hat = model(X)
        loss = loss_fn(Y_hat, Y)
        loss.backward() # backpropagation(미분)
        optimizer.step() # updates weights
    print(f"epoch : {epoch}, loss : {loss.item()}")


# 둘 중 하나는 파라미터만 저장
torch.save(model, 'mnist_cnn.pth') # 모델 아키텍처 + 파라미터 저장
torch.save(model.state_dict(), 'mnist_cnn.pt') # 파라미터만 저장


##################################################################################
# # 모델 로드
# # 잘 맞추는지 테스트
# # Accuracy 확인

# model = torch.load('./mnist_clf.pth', weights_only=False)

# for i in range(20):
#     img = transforms(mnist_test[i][0])
#     print(mnist_test[i][1])
#     plt.imshow(img, cmap='gray')
#     plt.show()

#     # [i] 인덱스, [0]: 이미지데이터, [1]: 라벨(GT)
#     x_test = mnist_test[i][0]
#     print(x_test.shape, x_test.dim, type(x_test))

#     # 형태 변환을 해주어야 함.
#     x_test = x_test.view(-1, 784)
#     prediction = model(x_test)
#     print(prediction) #
#     prob = F.softmax(prediction, dim=1)
#     print(prob)
#     print(torch.argmax(prob, dim=1))
#     print()

