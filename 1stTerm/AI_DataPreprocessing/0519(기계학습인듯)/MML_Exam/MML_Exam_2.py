# 2. 입력층에 있는 weight들이 출력 층의 Error에 미치는 영향을 계산하기 위해서
    # Chain-Rule을 이용한 Backpropagation을 수행하여야 한다.
    # 다음과 같은 신경망이 주어졌을 때
    # Backpropation에 의해 업데이트 되는 Weight들을 구하는 코드를 작성

##########################################################################

# 조건 1: Weight 5,6,7,8 이 Total Error에 미치는 영향을 구하는 코드만 작성하시오.
# 조건 2: Forward phase에서 계산되어지는 값은 미리 계산해놓고,
#        z3, z4를 W5, W6, W7, W8로 편미분한 값도 미리 계산해놓는다.
# 조건 3: Sigmoid 함수는 별도로 만들어서 사용하며, Learning Rate 값은 0.5로 세팅한다.

##############################################################################

import numpy as np

wVal = [0.2, 0.23, 0.38, 0.35, 0.42, 0.32, 0.64, 0.6]

w1 = wVal[0]
w2 = wVal[1]
w3 = wVal[2]
w4 = wVal[3]
w5 = wVal[4]
w6 = wVal[5]
w7 = wVal[6]
w8 = wVal[7]

import math


def sigmoid(val):
    return 1/(1 + np.exp(val))

lr = 0.5
x1, x2, x3, x4 = 0.1, 0.2, 0.3, 0.4

h1 = sigmoid(x1)
h2 = sigmoid(x2)

target_o1=0.4
target_o2=0.6

z1 = w1*x1 + w2*x2
z2 = w3*x1 + w4*x2

z3 = w5*h1 + w6 *h2
dz3_w5 = h1
dz3_w6 = h2
"""dz3_w7 = h2
dz3_w8 = h2"""

z4 = w7*h1 + w8*h2
dz4_w7 = h1
dz4_w8 = h2
o1 = sigmoid(z3)
o2 = sigmoid(z4)

Eo1 = 0.5 * (target_o1 - o1) **2
Eo2 = 0.5 * (target_o2 - o2) **2
print("eo1",Eo1)
print("eo2", Eo2)
Etotal = Eo1 + Eo2


print(z1, z2, h1, h2, z3, z4, o1, o2, Etotal)



def backpropagation_1(weight, d_weight, target, output):
    # Etotal = (1/2)*(target - output)**2 +
    # output =  weight - lr*(weight/d_weight)
    # Etotal = 0.5*(target - output)**2
    # target - output

    # vus = (Etotal/target)*(target/d_weight)*(d_weight/weight)
"""
    a= (-1)*(target - output)
    a*=(output*(1-output))
    a*=d_weight

    b = weight - lr*a
    return b

"""

if __name__ == '__main__':
    print(backpropagation_1(w5, dz3_w5, target_o1, o1))
    print(backpropagation_1(w6, dz3_w6, target_o1, o1))
    """
    # print(backpropagation_1(w7, dz3_w7, target_o2, o2))
    # print(backpropagation_1(w8, dz3_w8, target_o2, o2))
    """
    """ 주석 처리한 부분은 2시 이후에 작성했습니다.
    backpropagation_1 함수 부분 통으로 도움 받아 작성했습니다...
    채점 시 제외 부탁드립니다 죄송합니다 감사합니다...."""