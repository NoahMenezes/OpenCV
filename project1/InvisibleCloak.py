import numpy as np
import cv2
import time

cap=cv2.VideoCapture(0)
# Make sure your camera resolution is 640x480, otherwise this might not save correctly
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('invisibility cloak.avi', fourcc, 20.0, (640, 480))

# Allow the camera to warm up
print("Starting the camera... Get ready!") # <-- ADDED LINE
time.sleep(2)

background=0
# Capture the background
print("Capturing background... Please move out of the frame!") # <-- ADDED LINE
for i in range(30):
    ret,background=cap.read()

print("Background captured successfully! You can now enter the frame. ✨") # <-- ADDED LINE
    
while(cap.isOpened()):
    ret,img=cap.read()
    
    if not ret:
        break
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # --- ADD THIS NEW BLOCK ---
    # Range for blue color
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    # --- END OF NEW BLOCK ---
    
    # Define the kernel once
    kernel = np.ones((3,3), np.uint8)
    
    # Use the kernel in the morphology functions
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel, iterations=2)
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_DILATE, kernel, iterations=1)

    # Invert the mask
    mask2=cv2.bitwise_not(mask1)
    
    # Segment out the cloak from the frame
    res1=cv2.bitwise_and(background, background, mask=mask1)
    # Segment the non-cloak part of the current frame
    res2=cv2.bitwise_and(img, img, mask=mask2)
    
    # Combine the background and the current frame
    final_output = cv2.add(res1, res2)
    out.write(final_output)
    cv2.imshow('Invisible Cloak', final_output)
    
    # Use a single waitKey to avoid issues
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
    # Check if the window was closed by the user
    if cv2.getWindowProperty("Invisible Cloak", cv2.WND_PROP_VISIBLE) < 1:
        break

print("Exiting program.")
cap.release()
out.release()
cv2.destroyAllWindows()