import numpy as np
import cv2
import time

cap=cv2.VideoCapture(0)
# Make sure your camera resolution is 640x480, otherwise this might not save correctly
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('invisibility cloak.avi', fourcc, 20.0, (640, 480))

# Allow the camera to warm up
time.sleep(2)

background=0
# Capture the background
for i in range(30):
    ret,background=cap.read()
    
while(cap.isOpened()):
    ret,img=cap.read()
    
    if not ret:
        break
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # Range for lower red
    lower_red=np.array([0,120,70])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red, upper_red)
    
    # Range for upper red
    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red, upper_red)
    
    # Combine the masks
    mask1=mask1+mask2
    
    # Define the kernel once
    kernel = np.ones((3,3), np.uint8)

    # Use the kernel in the morphology functions
    # CORRECTED LINE 1: Fixed np.ones() syntax and removed extra arguments
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # CORRECTED LINE 2: Fixed np.ones() syntax, removed extra arguments, and fixed typo (masl1 -> mask1)
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_DILATE, kernel, iterations=1)

    # Invert the mask
    mask2=cv2.bitwise_not(mask1)
    
    # Segment out the cloak from the frame
    res1=cv2.bitwise_and(background, background, mask=mask1)
    # Segment the non-cloak part of the current frame
    res2=cv2.bitwise_and(img, img, mask=mask2)
    
   
    # final_output = cv2.addWeighted(res1,1,res2,1,0)
    # cv2.imshow('Magic !!!',final_output)
    # if cv2.waitKey(1) == 13:
    #     break

# The rest of your code for displaying and saving the output would go here.
# For example:
    final_output = cv2.add(res1, res2)
    out.write(final_output)
    cv2.imshow('Invisible Cloak', final_output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.getWindowProperty("Invisible Cloak", cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
out.release()
cv2.destroyAllWindows()