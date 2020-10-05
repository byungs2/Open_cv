import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import glob

# 마우스 움직임에 따라 그림 그릴 수 있는 사용자 정의 함수
def on_mouse(event, x, y, flags, param) :
    #global oldx, oldy
    if flags == 0 :
        #oldx, oldy = x,y
        #cv2.line(param, (oldx, oldy),(x,y),(0,0,255),1)
        param[y][x] = 0
        cv2.imshow('image', param)
    elif flags == 1 :
        param[y][x] = (0,0,255)
        cv2.imshow('image', param)
    #elif event == cv2.EVENT_LBUTTONDOWN :
    #elif event == cv2.EVENT_LBUTTONUP :
# 도화지
img = np.ones((480,640,3), dtype = np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image',on_mouse, img)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()