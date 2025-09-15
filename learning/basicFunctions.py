import cv2
img=cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('Panda',img)
# Gray
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)
# # Blur
# blur=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)

# Edge Cascading

# edge=cv2.Canny(img,125,175)
# cv2.imshow('edge',edge)

# edge=cv2.Canny(blur,125,175)
# cv2.imshow('edge',edge)

# dilated=cv2.dilate(img,(3,3),iterations=1)
# cv2.imshow('Dilated',dilated)

# eroded=cv2.erode(dilated,(7,7),iterations=3)
# cv2.imshow('Eroded',eroded)

# resize=cv2.resize(img, (500,500),interpolation=cv2.INTER_AREA)
# cv2.imshow('Resized',resize)

# resize1=cv2.resize(img, (500,500),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('resize1',resize1)
cv2.waitKey(0)


