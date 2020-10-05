import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import glob

def on_level_change(pos) :
    value = (255/16) * pos
    img[:,:] = np.clip(value, 0 , 255)
    cv2.imshow('image', img)


img = np.zeros((480,640,3), dtype = np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()