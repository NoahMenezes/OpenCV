import cv2
# Reading images
img = cv2.imread("C:/Users/Noah/Downloads/panda.jpg")
cv2.imshow('Panda',img)
cv2.waitKey(0)
# Reading Video
capture=cv2.VideoCapture("C:/Users/Noah/Downloads/13853907_360_640_25fps.mp4")
cv2.waitKey(0)
while True:
    isTrue,frame=capture.read()
    cv2.imshow('Video',frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
