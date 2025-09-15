import cv2
# import matplotlib.pyplot as plt
img=cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('Img',img)
# plt.imshow(img)     #Using matplotlib, BGR converted to RGB
# plt.show()          


# # BGR to GrayScale
# gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)

# # BGR to HSV
# hsv=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# cv2.imshow('HSV',hsv)

# # BGR to LAB
# lab=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB',lab)

# #BGR to RGB
# rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB',rgb)

# # HSV to BGR
# hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
# cv2.imshow('HSV --> BGR:',hsv_bgr)
# # LAB to BGR
# lab_bgr=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
# cv2.imshow('LAB --> BGR:',lab_bgr)


cv2.waitKey(0)