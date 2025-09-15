import cv2
import winsound

webcam=cv2.VideoCapture(0)
while True:
    _, im1=webcam.read(0)
    _, im2=webcam.read(0)
    