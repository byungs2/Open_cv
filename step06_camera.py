# 카메라에서 캡쳐한 이미지를 동영상 파일로 저장하기

import cv2
import matplotlib.pyplot as plt
import sys
import glob
import time

cap = cv2.VideoCapture(0)
if cap.isOpened() == False : 
    print("CAN NOT USE CAMERA")
    sys.exit()
else :
    print("CAN USE CAMERA")

ret, img_frame = cap.read()
if ret == False :
    print('Fail')
    sys.exit()

# 코덱 - 데이터 스트림 또는 신호에 대해 인코딩 또는 디코딩 혹은 둘다 다룰 수 있는 
# 적용 가능한 코덱 DIVX, XVID, MJPG, ...
# 동영상 파일을 위한 코덱 설정
# or cv2.VideoWriter_fourcc(*'MJPG')
codec = cv2.VideoWriter_fourcc('D','I','V','X')
# 프레임 레이터 :  디스플레이 장치가 화면 하나의 데이터를 표시하는 속도
fps = 30.0
h, w = img_frame.shape[:2]

writer = cv2.VideoWriter('playdata.avi', codec, fps, (w, h))

if writer.isOpened() == False :
    print('Fail')
    sys.exit()

while True :
    ret, img_frame = cap.read()
    
    if ret == False :
        print("Fail Capture")
        break
    writer.write(img_frame)
    cv2.imshow('Color', img_frame)
    
    if cv2.waitKey(1) == 27 :
        break
    
writer.release()
cap.release()
cv2.destroyAllWindows()
