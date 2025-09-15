import cv2
import numpy as np
img=cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('Panda',img)
if img is None:
    print("❌ Image could not be loaded. Check the file path.")
    exit()
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1], img.shape[0])
#     return cv2.warpAffine(img,transMat,dimensions)

# -x-->Right
# -y-->Up
# x-->Left
# y-->Down
# translated=translate(img, 20,20)
# cv2.imshow('New_Image',translated)
# resize1=cv2.resize(translated, (500,500),cv2.INTER_CUBIC)
# cv2.imshow('Resize1',resize1)

# Rotation
# def rotate(img,angle, rotPoint=None):
#     (height,width)= img.shape[:2]
#     if rotPoint is None:
#         rotPoint=(width//2,height//2)

#     rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions=(width,height)
#     return cv2.warpAffine(img,rotMat,dimensions)

# rotated=rotate(img,-45)
# cv2.imshow('Rotated',rotated)
# rotated_rotated=rotate(rotated,-45)
# cv2.imshow('Image',rotated_rotated)


# Resizing

# resized=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Resize',resized)

# Flipping

# flip=cv2.flip(img,flipCode=0)  #0-Vertically, 1= Horizontally y, -1=Both Horizontal and Vertical
# cv2.imshow('Flip',flip)

# Cropping
# cropped=resized[100:200, 200:300]
# cv2.imshow('cropped',cropped)
cv2.waitKey(0)
