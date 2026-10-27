import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1) #시작점(생략시0), 끝점(미포함), step size(생략시 1)
    y = sigmoid(x)

    plt.plot(x, y)
    plt.plot([0,0], [1,0], ":")
    plt.title('Sigmoid Function')
    plt.show()