# median filter / selected sort algorithm 구현해보기.
import numpy as np
'''
def select_sort(in_data):
    for i in range(len(in_data)):
        for j in range(len(in_data)):
            med = in_data[i:i+3, j:j+3].median()
            in_data[i,j]=med
    return in_data

def median_filter(in_img):
    select_sort(in_img)
    return in_img
    pass
'''

import cv2
import pandas as pd
import math
import numpy as np

noise_img = cv2.imread("C:/Users/AI-00/Desktop/salt-pepper-noise.jpg")
#noise_img = cv2.imread('C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0511/saltandpepperlena-300x300.jpg')

#print(type(noise_img), noise_img.shape())

input_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
# def Sep3X3():


# def FindMin():
    # med_3x3 =
size_ = int(input("몇 x 몇으로 걸러낼건가? 숫자만 입력하라.: "))


# filter_img = median_filter(input_img)
for i in range(len(input_img)):
    # print(f"\ninput_img[{i}]\n")
    for j in range(len(input_img)):
            if (i+size_<=len(input_img[i])) & (j+size_<= len(input_img[j])):
                med = input_img[i:i + size_, j:j + size_]
                # print(f"\ninput_img[{i}][{j}]")
                # print("med\n",med)

                print(f"원래: \n{med}")
                tmp_list = []
                for k in range(len(med)):
                    for l in range(len(med)):
                        tmp_list.append(med[k][l])
                    # for m in range(len(tmp_list)):
                    #     if tmp_list[k]<tmp_list[m]:
                    #         tmp_list[m] = tmp_list[j]
                    #         tmp_list[j]=tmp_list[k]

                        for m in range(len(med)):
                            if med[k][l]<med[k][m]:
                                tmp = med[k][m]
                                med[k][m] = med[k][l]
                                med[k][l] = tmp
                        # if ( hold < med[k][l] ).any():
                        #     tmp = med[k][l]
                        #     med[k][l] = hold
                        #     med[k][l] = tmp
                        # else:
                        #     continue
                print(f"정렬 후:\n {med}")
                print(f"중앙값: {med[(len(med)//size_)+1][(len(med)//size_)+1]}")
                # print("Mini: ",Mini)


                print()
            #print(med,"\n")

# print(type(med), "\n")



exit()
print(type(input_img.shape))
print(input_img[0],"\n", len(input_img[0]))
# print(input_img[0:3, 0:3],"\n", len(input_img[0:3, 0:3]))
print(input_img[1],"\n", len(input_img[1]))
print(input_img,"\n",len(input_img))


cv2.imshow("noise_img", noise_img)
cv2.waitKey()