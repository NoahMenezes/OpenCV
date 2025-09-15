import cv2
import numpy as np
img=cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('Pandas',img)

# blank=np.zeros(img.shape,dtype='uint8')
# cv2.imshow('Blank',blank)
# gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)

# blur=cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)
# canny=cv2.Canny(img, 125, 175)
# cv2.imshow('Canny Edges',canny)

# or

# ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
# cv2.imshow('Thresh',thresh)

# contours, hierarchies= cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found !')

# cv2.drawContours(blank,contours,-1, (0,0,255),1l)
# cv2.imshow('Contours Drawn',blank)
cv2.waitKey(0)

# Threshold- Binarizing Image
