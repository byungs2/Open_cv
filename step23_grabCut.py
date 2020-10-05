import sys
import cv2
import numpy as np
# Window Naming
cv2.namedWindow('src')

src = cv2.imread('imglist/nemo.jpg')

rc = cv2.selectROI('src', src)
print(rc)

mask = np.zeros(src.shape[:2], np.uint8)

# mask : cv2.GC_BGD 0 , cv2.GC_FGD 1, cv2.GC_PR_BGD 2, cv2.GC_PR_FGD 3
# rc : ROI -> cv2.GC_INIT_WITH_RECT 를 사용해야만 사용 가능
# None : 임시 배경 모델 행렬
# None : 임시 전경 모델 행렬
# IterCount : 반복 횟수를 결정하는 @Param
# Mode : cv2.GC_INIT_WITH_RECT

mask = mask[:,:,np.newaxis]
x = rc[0]
y = rc[1]
w = rc[2]
h = rc[3]

cv2.grabCut(src, mask, rc, None, None, 1, cv2.GC_INIT_WITH_RECT)

mask = np.where((mask == 0) | (mask == 2) , 255, 1).astype(np.uint8)
# mask = mask/3
dst = np.clip(src * mask.astype(float),0, 255).astype(np.uint8)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.imshow('src',src)


cv2.waitKey()
cv2.destroyAllWindows()