import cv2
import matplotlib.pyplot as plt
import sys
import glob

img1 = cv2.imread('imglist/cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('imglist/cat.jpg', cv2.IMREAD_COLOR)

if img1 is None or img2 is None :
    print('Error')
    sys.exit()


