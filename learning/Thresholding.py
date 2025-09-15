import cv2
img=cv2.imread("C:/Users/Noah/Downloads/astheticMen.jpg")
cv2.imshow('IMG',img)

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

# Simple thresholding
threshold, thresh=cv2.threshold(gray,100,255, cv2.THRESH_BINARY)
cv2.imshow('Simple Threshold',thresh)
# Simple thresholding inverse
threshold, thresh_inv=cv2.threshold(gray,100,255, cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Thresholded Inverse',thresh_inv)

# Adaptive Thresholding
adaptive_threshold=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, C=5)
cv2.imshow('Adpative Thresholding',adaptive_threshold)
cv2.waitKey(0)