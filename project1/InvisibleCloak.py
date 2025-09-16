import numpy as np
import cv2
import time

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('invisibility cloak.avi', fourcc, 20.0, (640, 480))

time.sleep(2)

background=0
for i in range(30):
    ret,background=cap.read()
    
while(cap.isOpened()):
    ret,img=cap.read()
    
    if not ret:
        break
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # hsv_values
    
    lower_red=np.array([0,120,70])
    upper_red=np.array([10,255,255])
    
    mask1=cv2.inRange(hsv,lower_red, upper_red)
    
    