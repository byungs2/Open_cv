import cv2
import matplotlib.pyplot as plt
import sys
import glob

src = cv2.imread('imglist/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('imglist/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('imglist/field.bmp', cv2.IMREAD_COLOR)

cv2.imshow('src',src)
cv2.imshow('mask',mask)

cv2.copyTo(src, mask, dst)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()