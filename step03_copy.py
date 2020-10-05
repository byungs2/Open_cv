import cv2
import matplotlib.pyplot as plt
import sys
import glob

img1 = cv2.imread('imglist/hsv.png')
img2 = img1
img3 = img1.copy()


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey()
cv2.destroyAllWindows()
