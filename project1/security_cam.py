import cv2
import winsound

# Open webcam
webcam = cv2.VideoCapture(0)
# Read the first frame
_, im1 = webcam.read()
im1=cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
while True:
    _, im2 = webcam.read()
    im2_gray=cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    
    diff = cv2.absdiff(im1, im2_gray)
    _,thresh=cv2.threshold(diff,20,255, cv2.THRESH_BINARY)
    contours, _=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        winsound.Beep(500, 100)
        
        
    cv2.imshow("Security camera", diff)
    # Update the previous frame
    im1 = im2_gray.copy()
    if cv2.waitKey(10)  ==27:
        break
    if cv2.getWindowProperty("Security camera", cv2.WND_PROP_VISIBLE) < 1:
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()
