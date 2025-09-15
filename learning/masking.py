import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('IMG', img)

# Create a blank mask (same height and width as the image, single channel)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('Blank Image', blank)

circle=cv2.circle(blank, (img.shape[1]//2 +45,img.shape[0]//2),100,255,-1)
# cv2.imshow('Mask',mask)

rectangle=cv2.rectangle(blank, (30,30),(370,370),255,-1)

weird_shape=cv2.bitwise_and(circle,rectangle)
cv2.imshow('Weird Shape',weird_shape)


masked=cv2.bitwise_and(img,img,mask=weird_shape)
cv2.imshow('Masked Image',masked)

cv2.waitKey(0)



