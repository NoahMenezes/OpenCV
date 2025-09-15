import cv2
import numpy as np
# 3 is height,width and number of channels

# blank=np.zeros((500,500,3),dtype='uint8')
# cv2.imshow('Blank',blank)
# Paint the image as certain colour


# blank[:]=0,255,0
# cv2.imshow('Color',blank)

# blank[:]=255,0,0                                          #  Note: color order is not RGB here, it's BGR
# cv2.imshow('Blue',blank)

# blank[:]=0,0,0
# blank[200:300, 300:400]=0, 0, 255
# cv2.imshow('Box',blank)

# Draw a rectangle
# cv2.rectangle(blank,(0,0),(500,500),(0,255,0),thickness=2)
# cv2.imshow('Rectangle',blank)

# cv2.rectangle(blank,(0,0),(400,400),(0,255,0),thickness=-1)  # cv2.FILLED OR -1
# cv2.imshow('Rectangle_new',blank)

# cv2.rectangle(blank,(0,0),(500,blank.shape[0]//2),(0,0,255),thickness=-1)
# cv2.imshow('Editted',blank)

# Draw a circle
# cv2.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=10)
# cv2.circle(blank,(250,250),100,(255,0,0),thickness=-1)
# cv2.imshow('Circle',blank)

# Draw a line

# cv2.line(blank,(0,0),(400,400),(250,250,250),thickness=4)
# cv2.imshow('Line',blank)

# Write text
# cv2.putText(blank, 'Hello, My Name is Noah',(50,200),cv2.FONT_HERSHEY_COMPLEX,1.0, (0,255,0),2,)
# cv2.imshow('Text',blank)

# cv2.waitKey(0)
