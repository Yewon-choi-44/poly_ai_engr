import sys
import cv2
import numpy as np
import time 

img = cv2.imread("./20260917_0615170.jpg")
print(type(img))
print(img.shape)
#BGR 원점 화소값 확인
print(img[0,0,0], img[0,0,1], img[0,0,2])


if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

p2p_arr = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)



start = time.time()
for h in range(img.shape[0]):
    print(h)

end = time.time()
print(f"{end - start} seconds")



start = time.time()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
end = time.time()

print(f"opencv convert color: {end - start} seconds")
gray_resize = cv2.resize(gray, (500,500))
img_resize = cv2.resize(img, dsize=(500,500), fx=0.5, fy=0.5)

cv2.imshow('display', img)
cv2.imshow('img-resize', img_resize)
cv2.imshow('gray-display', gray_resize)
# cv2.imshow('gray-p2p', p2p_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()