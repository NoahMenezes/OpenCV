# Face detection using haarCascading xml code
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

img=cv2.imread("C:/Users/Noah/Downloads/img4.jpg")
cv2.imshow('Group',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

harr_cascade=cv2.CascadeClassifier('harr_face.xml')
faces_rect=harr_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+y,w+h),(0,255,0),thickness=2)

cv2.imshow('Detected faces',img)
cv2.waitKey(0) 