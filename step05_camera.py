import cv2
import matplotlib.pyplot as plt
import sys
import glob
import time

cap = cv2.VideoCapture(0)
if cap.isOpened() == False : 
    print("CAN NOT USE CAMERA")
    sys.exit()
else :
    print("CAN USE CAMERA")

while True :
    time.sleep(1)
    ret, img_frame = cap.read()
    
    if ret == False :
        print("Fail Capture")
        break
    cv2.imshow('Color', img_frame)

    if cv2.waitKey(1) == 27 :
        break
cap.release()
cv2.destroyAllWindows()
