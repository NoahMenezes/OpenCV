import cv2
import winsound

# Open webcam
webcam = cv2.VideoCapture(0)  # Start capturing video from the default camera (usually the built-in webcam)

# Capture the first frame from the webcam
_, im1 = webcam.read()

# Convert the first frame to grayscale for easier processing (color not needed for motion detection)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

motion_counter = 0  # Initialize a counter to keep track of how many times motion has been detected

while True:
    # Capture the next frame from the webcam
    _, im2 = webcam.read()
    
    # Convert the current frame to grayscale (to match the first frame)
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the previous frame and the current frame
    # This highlights the areas where there is a change (motion)
    diff = cv2.absdiff(im1, im2_gray)
    
    # Apply a binary threshold to the difference image
    # Pixels with intensity greater than 20 are set to 255 (white), others set to 0 (black)
    # This step creates a clear mask of motion areas
    _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
    
    # Find contours in the thresholded image
    # Contours are outlines of the detected motion areas
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected_this_frame = False  # Flag to ensure motion counter increases only once per frame

    # Loop through each detected contour (motion area)
    for c in contours:
        # Ignore small contours to reduce noise and false positives
        # 5000 is an arbitrary area threshold; increase/decrease to tune sensitivity
        if cv2.contourArea(c) < 5000:
            continue
        
        # If motion has not yet been detected in this frame, count it and beep
        if not motion_detected_this_frame:
            motion_counter += 1  # Increment motion detection counter
            print(f"Motion detected! Count: {motion_counter}")  # Print motion count to console
            winsound.Beep(500, 100)  # Play a beep sound at 500 Hz for 100 milliseconds
            motion_detected_this_frame = True  # Prevent multiple counts in one frame

    # Display the motion count text on the difference image (diff)
    # Parameters: image to draw on, text string, position, font, font size, color (white), thickness
    cv2.putText(
        diff,                            # image to draw on
        f"Motion Count: {motion_counter}",  # text to display
        (10, 30),                       # position (x=10, y=30) near top-left corner
        cv2.FONT_HERSHEY_SIMPLEX,       # font style
        1,                             # font scale (size)
        (255, 255, 255),               # text color (white)
        2                              # thickness of text stroke
    )

    # Show the difference image in a window titled "Security camera"
    cv2.imshow("Security camera", diff)
    
    # Update the previous frame to be the current grayscale frame for the next loop iteration
    im1 = im2_gray.copy()

    # Wait for 10 ms for a key press
    # If 'ESC' key (ASCII 27) is pressed, exit the loop
    if cv2.waitKey(10) == 27:
        break

    # If the display window is closed manually, exit the loop
    if cv2.getWindowProperty("Security camera", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
