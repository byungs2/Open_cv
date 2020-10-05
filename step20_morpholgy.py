import sys
import cv2
import numpy as np
#침식, 팽창

src = cv2.imread('imglist/Cube.png', cv2.IMREAD_GRAYSCALE)

# (사각형 모양 구조 3행 5열)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(src, se)
dst2 = cv2.dilate(src, None)

cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)


cv2.waitKey()
cv2.destroyAllWindows()