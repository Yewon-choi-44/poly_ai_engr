"""
1. Mousecallback 함수 이용
2. labelme 유사한 프로그램 만들기
3. YoLo label.txt 파일 형태가 출력될 수 있도록 => label.txt(GT, Target)
4. annotation.txt(class, x, y, w, h)
5. YOLO IMG grid
"""

import cv2
import sys

img = cv2.imread("./vehicle dataset/train/images/0CCFZ9DKVLND.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

def draw(event, x, y, flags, param):
    global ix,iy

    if event==cv2.EVENT_FLAG_LBUTTON:
        # cv2.rectangle(img, (x,y), (x+200, y+200), (0,0,255),2)
        ix, iy= x, y
    elif event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix,iy), (x, y), (0, 0, 255), 2)
    cv2.imshow('Drawing', img)
    print(f"{x}, {y}, {ix}, {iy}")

cv2.namedWindow('Drawing')
cv2.imshow('Drawing', img)

cv2.setMouseCallback('Drawing', draw)

while(True):
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break


"""# import sys
# import os
# import numpy as np
# import cv2 as cv



# ################################################################
# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1
#  #######################################################
# # mouse callback function
# def mouse_click(event,x,y,flags,param):
#     global ix,iy,drawing,mode
 
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
 
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv.circle(img,(x,y),5,(0,0,255),-1)
 
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv.circle(img,(x,y),5,(0,0,255),-1)
# ########################################################
# img = np.zeros((512,512,3), np.uint8)
# # img = np.zeros((512,512,3), np.uint8)
# # cv.namedWindow('image')
# # cv.setMouseCallback('image',draw_circle)

# # while(1):
# #     cv.imshow('image',img)
# #     k = cv.waitKey(1) & 0xFF
# #     if k == ord('m'):
# #         mode = not mode
# #     elif k == 27:
# #         break



# img_path = "./vehicle dataset/train/images"
# img_list = os.listdir(img_path)
# # txt_path = 

# for img in img_list:
#     img_path = os.path.join(img_path, img)
#     # cv.imshow("image", img)
#     cv.namedWindow('image')
#     cv.setMouseCallback('image',mouse_click)

#     while True:
#         if cv.waitKey(0): break

# cv.destroyAllWindows()
"""