import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:/Users/Noah/Downloads/astheticMen.jpg")
cv2.imshow('IMG',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

mask=cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv2.imshow('Mask',mask)
# GrayScale Histogram
gray_hist=cv2.calcHist([gray],[0],mask=None,histSize=[256],ranges=[0,256])

masked=cv2.bitwise_and(gray,gray,mask=mask)
cv2.imshow('Mask',masked)


plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Color Histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i, col in enumerate(colors):
    hist=cv2.calcHist([img],[i],mask, [256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
