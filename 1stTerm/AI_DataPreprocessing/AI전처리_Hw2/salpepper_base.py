import numpy as np
import cv2
import sys
# import pandas as pd

np.set_printoptions(threshold=sys.maxsize)

def select_sort(in_data):
    # n = len(in_data)
    # tmpList = []

    # for문 추가 해서 nxn으로 묶고 sort해야 할 것 같음... 아닐 수도 있음
    #
    # print(in_data)
    in_data = [item for row in in_data for item in row]
    for i in range(len(in_data)):
        list_val = []
        min_val = min(in_data[i:])
        # print(min_val)
        min_idx = in_data.index(min_val,i)
        # print(min_val)
        in_data[i], in_data[min_idx] = in_data[min_idx], in_data[i]
        # print(f"{i},{j}: {in_data}")
                # tmpList.append(in_data[i][j])

    # min_val = in_data[len(in_data)//2]
    # print(len(in_data))
    min_val = in_data[(len(in_data) // 2)+1]
    return min_val
    # return tmpList
        # print(f"{i+1}회전 결과 \n: {in_data}")
###################################################################

def median_filter(in_img,n):
    filter_img = in_img.copy()
    for k in range(1,len(in_img)-1):
        for l in range(1,len(in_img)-1):
            # select_sort(in_img[0+k:3*k, 0+k:3*k])
            # a = k - int(len(n//2))
            # selSort = select_sort(in_img[k-a:k+a, l-a:l+a]
            #                       [k-a:k+a, l-a:l+a])
            selSort = select_sort(in_img[k:k+n, l:l+n])
            # print(in_img[k:k+n, l:l+n])
            # print(selSort)
            # print(f"k:{k},l:{l}")
            # print(selSort)
            filter_img[k,l] = selSort
            # print(len(mFilter))
    return filter_img

# 0~300 0~300
# (1,1) ~ (299,299)




###################################################################
noise_img = cv2.imread("C:/Users/AI-00/Desktop/salt-pepper-noise.jpg")
# noise_img = cv2.imread('C:/Users/AI-00/Desktop/하이테크_/AI데이터qw전처리실습/0511/saltandpepperlena-300x300.jpg')


n = int(input("nxn으로 필터를 맥일 겁니까? 숫자만 입력하세여:"))
input_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
# a = input_img[0:0+n,0:0+n][0:0+n,0:0+n]
# b = input_img[0:0+n,1:1+n][1:1+n,0:0+n]
# print(a)
# print(b)

# # print(input_img)
# # # # print(len(input_img))
filter_img = median_filter(input_img, n)
median_filter(input_img, n)
# print(f"filter_img,{filter_img}")
# # tmpList = median_filter(input_img)
# # print(type(input_img.shape))
# filter_img = np.uint8(filter_img)
# cv2.imshow("noise_img", noise_img)
# cv2.imshow("filter_img", filter_img)
cv2.imwrite(r"C:\Users\AI-00\Desktop\filter_img_77_.png", filter_img)

# #
# #
# cv2.imshow("input_img", filter_img)
# cv2.waitKey()

