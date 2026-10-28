import cv2 
import numpy as np

img = np.full((800,800,3), 255, dtype=np.uint8)
cv2.imshow("blank", img)

def mouse_click(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x,y) ,5, (0, 0, 255), 2)
        cv2.imshow("blank", img)
    elif event == cv2.EVENT_FLAG_RBUTTON:
        img = np.full((800, 800, 3), 255, dtype=np.uint8)
        cv2.imshow("blank", img)
cv2.setMouseCallback("blank", mouse_click)

while True:
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows()