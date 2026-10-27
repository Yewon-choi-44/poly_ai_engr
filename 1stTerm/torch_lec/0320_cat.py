import torch
#3D Tensor
#대표적인 예가 컬러 이미지
# w,h,c(width,height,channel)
#1920x1080x3(r,g,b)

import numpy as np
from PIL import Image

# img = Image.open("./cat.1.jpg") #./ 는 현재 디렉토리를 표현
img = np.array(Image.open("./cat.1.jpg").resize((100,100)))
# print()
img_tensor = torch.from_numpy(img)
print(img_tensor.size())
print(img_tensor.shape)
print(img_tensor.dim())

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()


#4-dimensional tensor
#폴더에 있는 여러 이미지를 텐서에 담으면 4d
#64x100x100x3 < 100x100x3한 이미지가 46장이 있다 > 이게 4차원이 되는 것

datapath= "/172.16.30.52/ai-data/2026_기계학습/dataset/training_set"
#경로에 있는 파일명들을 리스트에 넣기
#[cat1.jpg, cat2.jpg ...]
#[datapath+cat1.jpg, datapath + cat2.jpg...]
from glob import glob
# *.* 모든 확장자 + 모든 파일 test1.py
#*.py < - 확장자가 py인 모든 파일
cats = glob(datapath+"*") # cats = "dataset/training_set/cats/*"
print(cats[:2])
img_list = []
for cat in cats:
    img_list.append(np.array(Image.open(cat).resize((100,100))))

# ==> 리스트 중첩..으로 한 번 해보세요...

cat_arr = [np.array(Image.open(cat).resize((100,100))) for cat in cats[:20]]

# [ [img1-3d array],[img2-3d array],...,[img-n-3d array] ]
cat_tensor = torch.from_numpy(np.array(img_list))
print(cat_tensor.size())
print(cat_tensor.shape)
print(cat_tensor.dim())



# [7주차] 20260413(월) 기계학습프로그래밍
# 1초짜리 동영상은 30장의 이미지로 구성되어 있으며
# 30fps (frames per second)
# 5(초)x30x100x100x3 ==?



# Tensor의 개념, 사용법 등 확인헀음
# 많이 사용되는 연산 종류...
# 뻔하지만 헷갈릴 수 있을 법한 거 위주로 정리.
# 브로드캐스팅 (파이토치 개념)
# 행렬 A, B가 있습니다. 두 행렬에 대해 뎃셈, 뺄셈을 할 경우
# 두 행렬의 shape은 같아야 한다? 예. ==> 근디 파이토치에서는 달라도 알아서 계산해줌... --> 이걸 broadcasting이라고 한다...
# 사용 시 주의해서 사용할 것
m1 = torch.FloatTensor([[3,3]]) #1x2 행렬

# m2 = torch.FloatTensor([[2,2]]) #1x2 행렬
m2 = torch.FloatTensor([2]) #1x1 벡터
print(m1.shape, m2.shape) # 브로드캐스팅에 의해서 [[2, 2]]로 자동으로 확장 후 연산
print(m1+m2)

# m1 = 1x2, m2= 2x1 --> 덧셈 수행하면 몇x몇 나오나?
m1 =torch.FloatTensor([[1,2]]) #1x2
m2 =torch.FloatTensor([[3],[4]]) #2x1
print(m1+m2)


# result = torch.add(m1,m2) #결과(변수)에 꽂아줘야 저장이 되는거다.
# print(m1+2, m1)
# print(m1.add_(2),m1) <-- inplace옵션으로 사용하는 코드가 있음.
# 여러분들은 익숙하기 전까지는 사용x (단, 코드 리뷰할 때 보일 수 있으니... 참고할 것)



# 1) Matrix Multilpication,
# 2) Element_Wise곱(Multiplication: 같은 위치에 있는 것끼리 계산)
m1 = torch.FloatTensor([[1,2], [3,4]]) #2x2 행렬
#m2 = torch.FloatTensor([[1,2,3], [3,4,5]]) #2xn행렬 (2x3)
m2 = torch.FloatTensor([[1,2], [3,4]])
m3 = m1.matmul(m2) #matmul -> a매트릭스멀티플리케이션입니다.
m4 = m1 * m2 #m1.mul(m2) #Element_Wise곱
print(m3)
print(m4)
print(m3.shape)
print(m4.shape)


# 다음 시간에 gpu에서 20000x20000 매트릭스 연산하는 것과
# cpu에서 20000x20000 매트릭스 연산하는 것에 대한 처리 시간 체크
# 한 번 해보기.