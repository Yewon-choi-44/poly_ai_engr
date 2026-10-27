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
