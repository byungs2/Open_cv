import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# callback function of trackbar
def on_level_change(pos) :
    if pos == 0:
        cv2.imshow('src',src)
    else :
        src_copy = src_ycr.copy()
        dst = np.clip(src_ycr[:,:,0]*float(pos) - blr, 0, 255).astype(np.uint8)
        src_copy[:,:,0] = dst
        src_after = cv2.cvtColor(src_copy, cv2.COLOR_YCrCb2BGR)
        cv2.imshow('src',src_after)

# Window Naming
cv2.namedWindow('src')

# masking
src = cv2.imread('imglist/2/1.jpg', cv2.IMREAD_COLOR)
airplane = cv2.imread('imglist/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('imglist/mask_plane.bmp', cv2.IMREAD_COLOR)
src = cv2.resize(src, (600,400))
cv2.copyTo(airplane, mask, src)

# eyes_classifier
eyes_cascade = cv2.CascadeClassifier('C:\pyth\Lib\site-packages\cv2\data\haarcascade_eye.xml')
eyes = eyes_cascade.detectMultiScale(src, 10, 5)
cv2.rectangle(src,(30,30),(60,60),(255,0,0),2)

# Track Bar
cv2.createTrackbar('level', 'src', 0, 16, on_level_change)

#YCRCB
src_ycr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
blr = cv2.GaussianBlur(src_ycr[:,:,0],(0,0),2.0)



cv2.imshow('src',src)

cv2.waitKey()
cv2.destroyAllWindows()