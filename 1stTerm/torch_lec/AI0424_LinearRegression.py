import torch
import random
import numpy as np
import matplotlib.pyplot as plt #그림 그릴거라 추가


# 함수 작성 시에는 comment를 다는 습관을 들입시다.
#####################################################################
# 함수명: get_data
# input: None
# output/return: train_x, train_y (Type: Torch Tensor)
# 선형 방정식 y = ax+b 바탕으로 (a: gradient, b: intercept )
# 오차를 포함한 x,y 데이터 생성 후 생성된 데이터 반환
#####################################################################

def get_data():
    random.seed(424)
    #선형 방정식 계수(Coefficient)를 임의 지정
    grad = 2.3
    intercept = 0.88

    # 오차 범위: 10%
    gap = 0.1

    #number of Data: 20
    num_data_points = 20

    x_values = []
    y_values = []

    # x,y data 생성
    for i in range(num_data_points):
        #1. x 값 [1, 20] 중에서 랜덤으로 하나 추출
        x = random.uniform(1,20)

        #2. 직선방정식 + 랜덤 오차
        linear_eq = grad * x + intercept
        noise = random.uniform(1-gap, 1+gap)
        y = linear_eq * noise

        x_values.append(x)
        y_values.append(y)

    #list => numpy => torch tensor
    train_x = torch.from_numpy(np.array(x_values)).view(num_data_points, 1)
    train_y = torch.from_numpy(np.array(y_values))

    '''for i in range(len(train_x)):
        train_x[i] = train_x[i].type(torch.float)
        train_y[i] = train_y[i].type(torch.float)
    '''
    return train_x, train_y


#####################################################################
# 함수명: get_weights
# input: None
# output/return: 학습 파라미터인 w(weights), b(bias)
# 학습 파라미터를 랜덤으로 하나 지정
# requires_grad = True 셋팅 (w, b 모두)
#####################################################################

def get_weights():
    w = torch.randn(1) #랜덤으로 지정하든, 내가 지정하든 상관은 없다.
    b = torch.randn(1)

    w.requires_grad = True
    b.requires_grad = True

    return w, b


#####################################################################
# 함수명: simple_network
# input: None
# output/return: 학습 파라미터인 w(weight), b(bias)가 반영된 예측값
# H(train_x) = w*train_x + b
# torch.matmul 사용?
# 오차를 포함한 x,y 데이터 생성 후 생성된 데이터 반환
#####################################################################
def simple_network(x): # 카멜: (언더바로 구분하는게 아니라)
                       # simpleNetwork, trainX,lossFuc <- 이런식으로 이름 짓는 것.
    #w, b = get_weights()
    #h = torch.matmul(w, train_x) + b
    y_pred = torch.matmul(x.float(), w.float())+b
    return y_pred




#과제2: loss/cost function 등등의 함수에 대해 주석 작성해보기.
def loss_func(y_pred, y):
    loss = torch.mean((y_pred-y).pow(2).sum())
    #누적 미분 방지
    for param in [w, b]:
        if param.grad is not None:
            param.grad.data.zero_() #한번이라도 grad에 있는 데이터를 건드렸으면
                                    #그 다음에 수행할 땐 반드시 초기화를 하고 사용해야 한다.
    loss.backward() #미분하는 것.
    return loss.data



def param_update(lr):
    w.data = w.data - lr * w.grad.data
    b.data = b.data - lr * b.grad.data






if __name__ == '__main__': #원래 정상적인 방법으로 바꿔보라고 숙제를 내기 위해. 이걸 썼다.
    # 1. 학습 데이터 준비

    train_x, train_y = get_data()
    print(train_x.shape)
    print(train_y.shape)

    # 2. 학습 파라미터 셋팅
    w,b = get_weights()
    print(w.shape, b.shape)
    print(w, b)

    #epoch을 돌면서 수행항 함수
    #simple_network(train_x)
    # 과제1: 네임 스페이스를 자동으로 찾아가는 방식이 안되도록 함수 작성해볼것.
    # !최대한 지역변수로 구현해 볼 것.
    # simple_network(train_x)
    # 3. 하이퍼파라미터 셋팅
    learning_rate = 1e-6 #10의 -6승 #일반적으로 소수점으로 표현 안하고 <저렇게 표현함
                                    # 익숙해 지는 게 좋다.
    num_epochs = 1000

    # 그래프 그릴 대 필요한 값 지정
    loss_x = []
    loss_y = []


    # 4. 지정된 epoch 만큼 돌면서 경사타고 내려오는 것 구현.,..
    for epoch in range(num_epochs+1): #+1해주는 이유는 제일 마지막, 50번째가 뭔지 보고 싶기 때문이다.
       # 가설함수 "예측값"
       # 우리는 데이터를 20개만 사용했기 때문에 20x1 사이즈의 데이터를 예측
       y_pred = simple_network(train_x) #최초에 w,b가 곱해진 값이 들어갈거고.
                                        #이게 우리가 첫번째로 구해진 예측값이다.

       #loss 값 계산 및 미분
       loss = loss_func(y_pred, train_y)

       if epoch % 50 == 0: #로스값이 떨어지면 보통 print로 뽑는다.
           print(f"Current loss: {loss}")

       loss_x.append(epoch)
       loss_y.append(loss)

       #학습 파라미터 갱신
       param_update(learning_rate)

       #이렇게 하면 Epoch만큼 for문이 돌면서 학습이 될 것이다.
       #for문이 빠져나오면 그것이 학습이 완료된 상태가 될 것이다.


    # 5. 결과물 시각화
    print(w,b)


    plt.figure()
    # 데이터 분포와 추론된 모델의 파라미터로 그은 선
    plt.plot(train_x.detach().numpy(), train_y.detach().numpy(), 'ro', label = 'Data') #'ro' -> 색깔은 빨간색, 동그라미로 표현.ㅉ
    plt.plot(train_x.detach().numpy(), y_pred.detach().numpy(), 'b', label = 'Prediction')
    plt.legend()
    plt.title("Linear Regression")
    plt.show()

    plt.figure()

    # loss 값이 안정적으로 잘 떨어지는지 확인
    # learning_rate를 더 작게 할지 크게 할지 결정 가능
    plt.plot(loss_x.detach().numpy(), loss_y.detach().numpy())
    plt.title("Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()