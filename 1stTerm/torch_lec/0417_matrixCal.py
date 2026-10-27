
import torch.cuda
import torch
'''
print()
print(torch.cuda.is_available())
print(torch.cuda.device_count())

import time
start = time.time()
a = torch.rand(20000, 20000)
b = torch.rand(20000, 20000)
#c = a.matmul(b)
#end = time.time()
#print(f'CPU time: {end-start} first')

use_gpu = torch.cuda.is_available()
start = time.time()
if use_gpu:
    a = a.cuda()
    b = b.cuda() #GPU쓸 때는 뒤에 cuda()<-이걸 붙여서 GPU를 사용할 거야 하고 지정을 해줘야 함.
    a.matmul(b)
end = time.time()
print(f'GPU time: {end-start} seconds')


# 평균, max, argmax...
#a = torch.FloatTensor([1,2,3])

a = torch.FloatTensor([ [1,2], [3,4] ])
b = torch.FloatTensor([4,5,6,7])
print(a.mean(dim=0))
print(a.mean(dim=1))
print(a.sum(dim=0))
print(a.sum(dim=1))

a_ = torch.FloatTensor([ [1,4], [5,2] ])
print(a_.min(),a_.max())
print(a_.min(dim=0),a_.max(dim=0)) #dim=0은 행
print(a_.min(dim=1),a_.max(dim=1)) #dim=1은 열
print(a_.argmax()) #어떤 리스트든배열이든 자료형에서 최댓값이 있는 인댁스를 반환하는 것 - argmax()

#argmax 왜 쓰나?
#multi-variable classification
#개 고양이 돼지 곰 -> (돼지 그림) 여러 개 중에 하나를 물음
#컴퓨터는 010101을 인식하기에 그림을 읽기 위해 label.txt...로 되어있음...
#0 - 개 , 1 - 고양이 , 2- 돼지 , 3-곰 이렇게 정의가 되어있음
#이걸 di.model....에 넣고 나면 확률값으로 나온다... 이게... softmax라는 함수를 통해서... max로 나온다....
# 고양이일 확률 - 0.3 곰일 확률 0.5 개일 확률 0.1 돼지일 확률 0.1 -> sum = 1
# 30%의 확률로 이 그림은 고양이야, 50%의 확률로 이 그림은 곰이야...
# max값의 index값을 찾아서 이 인덱스가 몇 번째에 있다...를 찾아야 하는데 이 찾는게 argmax.이다.
# argmax = 1 인 것을 찾아가서, 이 그림은! 곰이네! 하고! 결정?해주는...거다.........
# argmax -> 확률이 가장 높은 것의 인덱스를 찾아 안내...한다고...
# 그래서...argmax를....자주...사용한다.....
'''
#############################################################################
# shape 변경을 많이 한다... 2x2x2 면 --> 4ㅌ2로 바꿔서 쓴다든지.... -> 1x2x4로 바까서 쓸 수 있다...
# 우리가 데이터의 형태를 바꿔야만 동작하는 코드들이 있어서...종종 바꿔서 사용한다....

#예제 2x2x3 짜리...

t = torch.FloatTensor([ [[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(t.shape) #torch.Size([2,2,3]) ==> 3d tensor
# 2d tensor ==> [4x3]
# view (reshape: numpy)
t2 = t.view([-1,3]) #-1의 의미 : 제일 끝의 인덱스, view/shape에서는 돈 케어라는 뜻.
                    #row는 상관이 없고 column만 3개만 맞춰주는 형태로 맞춰주면 돼.
                    #그리고 남은 건 알아서 계산해서 정리해줘.

t3 = t.view([-1,1,3]) #mx1x3에서  1, 3은 반드시 지키고 나머지는 알아서 계산
                      #원본은 2x2x3 ==> mx1x3 == > "4"x1x3
# t4 = t.view([-1,1,7]) # => 이케 하면 에러날거다...
print(t)
print(t2)
print(t2.shape)


#squeeze: nx1 --> n으로 만드는 거. (하나의 차수를 제거해주는 역할.)
t = torch.FloatTensor( [[0], [1], [2], [3]])
print(t)
t_sq = t.squeeze()
print(t_sq)




