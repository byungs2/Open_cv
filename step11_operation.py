import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import glob

src = cv2.imread('imglist/cat.jpg', cv2.IMREAD_GRAYSCALE)

src = cv2.resize(src,(300,300))
dst = cv2.add(src, 100)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

src2 = cv2.imread('imglist/cat.jpg')
src2 = cv2.resize(src2,(300,300))
dst2 = cv2.add(src2,(100,100,100,0))
cv2.imshow('src2',src2)
cv2.imshow('dst2',dst2)

#dst = np.clip(src + 100.,0,255).astype(np.unit8)

cv2.waitKey()
cv2.destroyAllWindows()
