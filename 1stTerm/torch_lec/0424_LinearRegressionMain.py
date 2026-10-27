import torch
import random
import numpy as np
import matplotlib.pyplot as plt #그림 그릴거라 추가
import AI0424_LinearRegression as Lin

train_X, train_Y= Lin.get_data()
'''print("\n\nlen(train_X)\n\n", len(train_X))
print("\n\nlen(train_Y)\n\n", len(train_Y))
print("\n\ntrain_X\n\n", train_X)
print("\n\ntrain_Y\n\n", train_Y)
'''

weights, bias = Lin.get_weights()
'''
print("\n\nweights\n\n", weights)
print("\n\nbias\n\n", bias)
'''

print(Lin.simple_network(train_X))