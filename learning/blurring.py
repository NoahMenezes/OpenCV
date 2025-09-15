import cv2

img=cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow("Img",img)
# # Averaging
# averaging=cv2.blur(img,(7,7))
# cv2.imshow('Averaging',averaging)

# # Gaussian Blur
# gauss=cv2.GaussianBlur(img, (7,7), 0)
# cv2.imshow('Gaussian Blur',gauss)

# # Median Blur
# median=cv2.medianBlur(img,7)
# cv2.imshow('Median',median)

# # Bilateral
# bilateral=cv2.bilateralFilter(img,5,15,15)
# cv2.imshow('Bilateral',bilateral)

cv2.waitKey(0)