import numpy as np
import cv2
import time

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('invisibility cloak.avi', fourcc, 20.0, (640, 480))

time.sleep(2)