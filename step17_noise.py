import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src = cv2.imread('newimage/noise.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('imglist/lenna.bmp')

# (입력 영상, 커널 크기[1보다 큰 홀수로 지정])
dst = cv2.medianBlur(src, 3)

# 양방향 블러링
dst2 = cv2.bilateralFilter(src2, -1, 1, 1)


cv2.imshow('src', src)
cv2.imshow('src2', src2)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()