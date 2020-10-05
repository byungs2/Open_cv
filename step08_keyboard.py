import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import glob

img = cv2.imread('imglist/cat.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)

while True :
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image',img)
    elif keycode == ord('q') :
        break

cv2.destroyAllWindows()