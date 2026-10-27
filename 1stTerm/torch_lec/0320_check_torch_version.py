import torch
'''#
#print(torch.cuda.is_available());
#print(torch.cuda.get_device_name(0));
#print(torch.cuda.device_count());
print(torch.__version__);

#Vector -- 1D(DImensional) Tensor
#금주의 평균 온도
temp = torch.FloatTensor([17.4,20,13.7, 17.4 , 20, 13.7, 20]);
print(temp.size());
print(temp.dim());
print(type(temp));

#type이 텐서라고 하더라도 리스트와 같이 인덱스, 슬라이싱 모두 가능
print(f"월,화 평균 온도는 {temp[0]}, {temp[1]} 입니다.");
#슬라이싱으로 화~목까지의 온도를 출력하세요. (시간될 때 해보기)
print();

#2D Tensor == Matrix
# 4x3 matrix
m = torch.FloatTensor([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ])
print(m.size());
print(m.dim());

#슬라이싱, 인덱싱 등 실습해보세요.
#첫 번째 차원의 모든 것(모든 로우와, 두번째 차원(col)의 두번째 값들만...)
print(m[:,1]);
#첫번째 차원의 3번째 요소들과 두번째 차원의 모든 것
#[[5, 6],[8,9]] <-- 이렇게 한 번 가지고 와보세요.
print(m[1][1:3],m[2][1:3]);

#t = [1,2,3,4,5];
#for i in range(len(t)):
   # print(t[i]);

#for i in range(7):
   # print(t[i]);

'''
from sklearn.datasets import fetch_california_housing
'''housing = fetch_california_housing();
print(type(housing));
print(type(housing.data));
print(housing.data.shape) #numpy type, mxn matrix
cal_tensor = torch.FloatTensor(housing.data);
cal_tensor = torch.from_numpy(cal_tensor);
print(cal_tensor.size());
print(cal_tensor.dim());
print(cal_tensor[:10. :])'''

#data=(20640, 8)
#train_x = data(70 ,7)
#train_y = data(i)

import sklearn.datasets