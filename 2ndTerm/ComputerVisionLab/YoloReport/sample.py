"""
# 1. Import the library
from inference_sdk import InferenceHTTPClient, InferenceConfiguration

# 2. Connect to your workspace
client = InferenceHTTPClient(
  api_url="https://serverless.roboflow.com",
  api_key="API_KEY"
).configure(InferenceConfiguration(
  api_key_transport="header"  # header-based auth (inference v1.5.0+)
))

# 3. Run your workflow on an image
result = client.run_workflow(
  workspace_name="<YOUR_WORKSPACE>",
  workflow_id="<YOUR_WORKFLOW_ID>",
  images={
    "image": "YOUR_IMAGE.jpg"  # Path to your image file
  },
  parameters={
    "classes": "car, truck, bus, bike, person"
  },
  use_cache=True  # cache workflow definition for 15 minutes
)

# 4. Get your results
print(result)

"""

######################################################
import numpy as np
import cv2 as cv
 
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
 
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
 
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()
######################################################
"""
import cv2
def on_mouse(event, x, y, flags, param):
    # event : 발생한 마우스 이벤트 종류 (예: 왼쪽 클릭, 마우스 이동 등)
    # x, y  : 마우스 커서의 윈도우 내 좌표
    # flags : 마우스 이벤트 발생 시 특수키 상태 (예: Shift, Ctrl 키 등)
    # param : setMouseCallback 함수에서 전달한 추가 데이터
    pass

# 윈도우 생성 및 이미지 표시
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse)  # 'image' 창에 콜백 함수 등록
"""
######################################################
"""
# MouseCallback
특정 윈도우 창에서 마우스 이벤트(클릭, 이동, 휠 등)가 발생했을 때 자동으로 호출되도록 사용자가 미리 정의해두는 함수

OpenCV 파이썬(Python) 기준 주요 구조
마우스 콜백을 사용하려면 콜백 함수 정의와 등록 함수 연결 두 단계가 필요합니다.

1. 콜백 함수 형식 (onMouse)
    def on_mouse(event, x, y, flags, param):
        # event : 발생한 마우스 이벤트 종류 (예: 왼쪽 클릭, 마우스 이동 등)
        # x, y  : 마우스 커서의 윈도우 내 좌표
        # flags : 마우스 이벤트 발생 시 특수키 상태 (예: Shift, Ctrl 키 등)
        # param : setMouseCallback 함수에서 전달한 추가 데이터
        pass
    
2. 콜백 등록 함수 (`cv2.setMouseCallback`)**
   import cv2

   # 윈도우 생성 및 이미지 표시
   cv2.namedWindow('image')
   cv2.setMouseCallback('image', on_mouse)  # 'image' 창에 콜백 함수 등록
"""