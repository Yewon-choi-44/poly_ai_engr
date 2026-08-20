import torch.nn as nn


class BinaryClassification(nn.Module): # 상속 받는 거임.
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim

        self.linear = nn.Linear(in_dim, out_dim)
        self.sigmoid = nn.Sigmoid()

    """
    model = BinaryClassification(2, 1)
    hx = model(x) : forward method로 수행됨.
    """

    def forward(self, x):
        return self.sigmoid(self.linear(x))

class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        # n : batch_Size
        # 1st layer
        # input img(mnist : 28*28*1)
        # conv --> (n, 28, 28, 32)
        # pool --> (n, 14, 14, 32)
        
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        # n : batch_Size
                # 2nd layer
                # input img(n, 14, 14, 32)
                # conv --> (n, 14, 14, 64)
                # pool --> (n, 7, 7, 64)

        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32,out_channels= 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        # Flatten Layer (Fully Connected Layer)
        # nn.Linear(7*7*64, 10)

        self.fc = nn.Sequential(
            nn.Linear(in_features=7*7*64, out_features=1024, bias=True),
            nn.ReLU(),
            nn.Linear(in_features=1024, out_features=512, bias=True),
            nn.ReLU(),
            nn.Linear(in_features=512, out_features=256, bias=True),
            nn.ReLU(),
            nn.Linear(in_features=256, out_features=10, bias=True)
            )

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.view(out.size(0), -1) # 64, 7*7*64 (제일 뒤 -1 : 알아서 계산하라 의미)
        out = self.fc(out) # fc: fully connected
        return out 