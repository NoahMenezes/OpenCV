import cv2
# Resizing and Rescaling
img=cv2.imread("C:/Users/Noah/Downloads/nature1_imresizer.jpg")
cv2.imshow('Panda',img)


# def rescaleFrame(frame,scale=0.75):
#     # Images, Videos and Live Videos
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimensions=(width,height)
#     return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

# def changeRes(width,height):
#     # Live video
#     capture.set(3,width)
#     capture.set(4,height)

# resized_image=rescaleFrame(img)
# cv2.imshow('Panda',resized_image)
# #Reading Video
# capture=cv2.VideoCapture("C:/Users/Noah/Downloads/3692634-hd_1920_1080_30fps.mp4")

# if not capture.isOpened():
#     print("❌ Error: Could not open video file.")
#     exit()
# cv2.waitKey(0)

# while True:
#     isTrue,frame=capture.read()
#     if not isTrue:
#         break
#     frame_resized=rescaleFrame(frame,scale=0.2)
#     cv2.imshow('Video',frame)
#     cv2.imshow('Video Resized',frame_resized)
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv2.destroyAllWindows()