import torch

from torch import nn, device
from torch import optim
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.functional as F


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

print(device)

mnist_train = dsets.MNIST(root='MNIST_data/',
                          train=True,
                          transform=transforms.ToTensor(),
                          download=True)

mnist_test = dsets.MNIST(root='MNIST_data/',
                         train=False,
                         transform=transforms.ToTensor(),
                         download=True)

data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                          batch_size=256,
                                          shuffle=True)


transform = transforms.ToPILImage()


model = nn.Sequential()
model.add_module('fc1', nn.Linear(28*28,512))
model.add_module('relu1', nn.ReLU())
model.add_module('fc1', nn.Linear(28*28, 256))
model.add_module('relu2', nn.ReLU())
model.add_module('fc3', nn.Linear(256, 10))

model = nn.Linear(28*28, 10)
# model = model.to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


def train(epoch):
    for data, gt in data_loader:
        data = data.view(-1,28*28)
        optimizer.zero_grad()
        y_hat = model(data)
        loss = loss_fn(y_hat, gt)
        loss.backward()
        optimizer.step()
    print(f"epoch {epoch}, loss: {loss.item()}")

train(50)
torch.save(model, 'mnist_softmax.pth')


model = torch.load('mnist_softmax.pth', weights_only=False)
for i in range(20):
    img = transform(mnist_train[i][0])
    # print(mnist_train[i][0])

    x_test = mnist_test[i][0]
    x_test = x_test.view(-1,784)
    prediction = model(x_test)

    prob = F.softmax(prediction, dim=1)
    print(prob)
    print(torch.argmax(prob, dim=1))
    print()


correct = 0
print(len(mnist_test))
for i in range(len(mnist_test)):
    x_test = mnist_test[i][0]
    x_test = x_test.view(-1, 784)
    prediction = model(x_test)
    prob = F.softmax(prediction, dim=1)
    gt = mnist_test[i][1]
    if torch.argmax(prob, dim=1) == gt:
        correct += 1
acc = (correct/len(mnist_test))*100
print(f"Accuracy: {acc:.4f}%")
# print(f'Accuracy: {accuracy:.4f}')