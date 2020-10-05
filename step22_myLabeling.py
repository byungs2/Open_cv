import sys
import cv2
import numpy as np

src = cv2.imread('imglist/Keyboard.jpg', cv2.IMREAD_GRAYSCALE)
_, src_bin = cv2.threshold(src,0 , 255, cv2.THRESH_OTSU)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
for i in range(1, cnt) :
    (x,y,w,h,area) = stats[i]
    (x_center,y_center) = centroids[i]
    if area > 250 :
        cv2.rectangle(dst,(x,y), (x+w,y+h), (0,255,255), 2)
        dst[int(y_center)-5:int(y_center)+6,int(x_center)-5:int(x_center)+6] = (0,255,255)
    else :
        continue

cv2.imshow('src_bin',src_bin)
cv2.imshow('src',src)
cv2.imshow('dst',dst)


cv2.waitKey()
cv2.destroyAllWindows()