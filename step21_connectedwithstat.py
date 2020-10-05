import sys
import cv2
import numpy as np

# cnt : 객체 개수
# labels : 라벨 맵 행렬, 입력 영상과 같은 크기
# stats : 각 객체의 바운딩 박스, 픽셀 개수를 담은 행렬
# centroids : 각 객체의 중심 위치 정보를 담은 행렬

src = cv2.imread('imglist/Pendant.png', cv2.IMREAD_GRAYSCALE)

# 이미지 이진화(Threshold 값을 설정하여 임계를 넘으면 255 아니면 0으로 바꾸는듯)
_, src_bin = cv2.threshold(src,0 , 255, cv2.THRESH_OTSU)

# connectedComponentsWithStats
cnt, labels, stats, centroids  = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt) :
    (x, y, w, h, area) = stats[i]
    if area != 1 :
        cv2.rectangle(dst,(x,y),(x+w,y+h),(0,255,255),3)
    else : 
        continue

cv2.imshow('src',src)
cv2.imshow('src_bin',src_bin)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()