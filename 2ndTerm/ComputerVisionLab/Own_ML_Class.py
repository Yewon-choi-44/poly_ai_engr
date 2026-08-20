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
        # input img(mnist : 28x28x1)
        # conv --> (n, 28, 28, 32)
        # pool --> (n, 14, 14, 32)
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)
        )