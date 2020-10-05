import sys
import cv2
import numpy as np

#마스크(커널)를  직접 수작업으로 생성해서 영상의 특징 추출

src = cv2.imread('imglist/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('이미지 로드 실패')
    sys.exit()

# 케니
dst = cv2.Canny(src, 100, 150)
cv2.imshow('dst', dst)
cv2.imshow('src', src)


# 소벨 함수
# dx = cv2.Sobel(src, -1, 1, 0, delta = 128)
# dy = cv2.Sobel(src, -1, 0, 1, delta = 128)

# cv2.imshow('dx',dx)
# cv2.imshow('dy',dy)
# cv2.imshow('src',src)


# kernel = np.array([
#     [-1, 0, 1],
#     [-2, 0, 2],
#     [-1, 0, 1]],dtype = np.float32)

# dx = cv2.filter2D(src, -1, kernel, delta= 128)

# cv2.imshow('src', src)
# cv2.imshow('dx',dx)

cv2.waitKey()
cv2.destroyAllWindows()