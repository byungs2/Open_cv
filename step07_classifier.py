import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT


eyes_cascade = cv2.CascadeClassifier('C:\pyth\Lib\site-packages\cv2\data\haarcascade_eye.xml')
while(True):
    # frame 별로 capture 한다
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eyes_cascade.detectMultiScale(gray, 1.2, 5)

    #인식된 얼굴 갯수를 출력
    print(len(eyes))

    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in eyes:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    #화면에 출력한다
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()