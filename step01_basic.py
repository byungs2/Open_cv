import cv2
import matplotlib.pyplot as plt
import sys
import glob

img_files = glob.glob('imglist\\*.png')
print(img_files)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cnt = len(img_files)
print(cnt)
idx = 0
while True :
    img = cv2.imread(img_files[idx])

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0 :
        break
    idx += 1
    cv2.imshow('image',img)
    if idx >= cnt :
        idx = 0
cv2.destroyAllWindows()

