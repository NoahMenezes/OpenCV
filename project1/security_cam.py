import cv2
import winsound

# Open webcam
webcam = cv2.VideoCapture(0)


while True:
    _, im1 = webcam.read()
    _, im2 = webcam.read()
    diff = cv2.absdiff(im1, im2)
    gray=cv2.cvtColor(diff, cv2.COLOR_BAYER_BG2GRAY)
    _,thresh=cv2.threshold(gray,20,255, cv2.THRESH_BINARY)
    cv2.imshow("Security camera", diff)
    if cv2.waitKey(10)  ==27:
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()
