import pandas as pd
#import torch
#dictionary type의 데이터 변수를 하나 만들자.
data={
    'name':['kim','lee','park'],
    'age':[23,25,39]
}

df = pd.DataFrame(data)
print(df)

'''import cv2

img = cv2.imread("test.jpg")'''
