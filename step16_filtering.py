import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src = cv2.imread('imglist/cat.jpg')
src = cv2.resize(src,(480,640))

# 밝기 정보, x , y로 이루어진 배열 YCRCB -> GRAY_SCALE로 변환하는 식과 같은 식으로 밝기 정보를 가져온다
src_ycr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
blr = cv2.GaussianBlur(src_ycr[:,:,0],(0,0),2.0)
dst = np.clip(src_ycr[:,:,0]*15.0 - blr, 0, 255).astype(np.uint8)
src_ycr[:,:,0] = dst
src = cv2.cvtColor(src_ycr,cv2.COLOR_YCrCb2BGR)

cv2.imshow('src_ycr',src_ycr)
cv2.imshow('dst',dst)
cv2.imshow('src',src)


cv2.waitKey()
cv2.destroyAllWindows()