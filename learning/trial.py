import cv2 as cv
import numpy as np
img=cv.imread('C:/Users/Noah/Downloads/kitten.jpeg')
cv.imshow('img',img)
# b,g,r=cv.split(img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

# print(img.shape)
# print(b.shape)
# print(r.shape)
# print(g.shape)

# blue=cv.merge([b,blank,blank])
# green=cv.merge([blank,g,blank])
# red=cv.merge([blank,blank, r])
# cv.imshow('blue',blue)
# cv.imshow('green',green)
# cv.imshow('red',red)
# merged=cv.merge([b,g,r])
# cv.imshow('merged',merged)

# bgr_rgb=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('bgr_rgb',bgr_rgb)
# bgr_hls=cv.cvtColor(img, cv.COLOR_BGR2HLS)
# cv.imshow('bgr_hls',bgr_hls)
# bgr_hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('bgr_hsv',bgr_hsv)
# bgr_lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('bgr_lab',bgr_lab)
# bgr_luv=cv.cvtColor(img, cv.COLOR_BGR2LUV)
# cv.imshow('bgr_luv',bgr_luv)
# # bgr_bgr565=cv.cvtColor(img, cv.COLOR_BGR2BGR565)
# # cv.imshow('bgr_bgr565',bgr_bgr565)
# # bgr_bgr555=cv.cvtColor(img, cv.COLOR_BGR2BGR555)
# # cv.imshow('bgr_bgr555',bgr_bgr555)

# average=cv.blur(img, (5,5))
# cv.imshow('average',average)
# medianBlur=cv.medianBlur(img, 5)
# cv.imshow('medianBlur',medianBlur)
# gaussianBlur=cv.GaussianBlur(img, (5,5), 15,15)
# cv.imshow('gaussianBlur',gaussianBlur)
# bilateralBlur=cv.bilateralFilter(img, 5,15,15)
# cv.imshow('bilateralFilter',bilateralBlur)


# canny=cv.Canny(img, 125,175)
# cv.imshow('canny',canny)
# dilated=cv.dilate(img, (5,5))
# cv.imshow('dilated',dilated)
# eroded=cv.erode(img, (5,5))
# cv.imshow('eroded',eroded)
# resize=cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('resize',resize)



blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 100, (255,255,255), thickness=-1)
cv.imshow('mask',mask)
masked=cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked',masked)


cv.waitKey(0)