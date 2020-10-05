import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# clip() : float 데이터 연산, 최대~ 최소 즉 값을 한정하는 함수
src = cv2.imread('imglist/cat.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.GaussianBlur(src,(0,0), 5)
dst2 = np.clip(src*2.0 - dst,0,255).astype(np.uint8)


cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

cv2.waitKey()
cv2.destroyAllWindows()


