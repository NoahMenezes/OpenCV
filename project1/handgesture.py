import cv2
import mediapipe
import pyautogui

# Initialize Mediapipe Hands solution with default parameters
capture_hands = mediapipe.solutions.hands.Hands()

# Drawing utility from Mediapipe to draw hand landmarks on the image
drawing_option = mediapipe.solutions.drawing_utils

# Get the screen size of the user's monitor
screen_width, screen_height = pyautogui.size()

# Start capturing video from the default webcam
camera = cv2.VideoCapture(0)

# Initialize variables for fingertip coordinates
x1 = y1 = x2 = y2 = 0

# Variables to smooth cursor movement for better user experience
prev_mouse_x = 0
prev_mouse_y = 0
smoothing_factor = 0.2  # Smaller value = smoother, but slower cursor movement

while True:
    # Read a frame from the webcam
    _, image = camera.read()

    # Get image dimensions
    image_height, image_width, _ = image.shape

    # Flip the image horizontally to create a mirror effect
    image = cv2.flip(image, 1)

    # Convert BGR image (OpenCV default) to RGB for Mediapipe processing
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hand landmarks
    output_hands = capture_hands.process(rgb_image)

    # Extract detected hand landmarks, if any
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        # Loop over each detected hand
        for hand in all_hands:
            # Draw the hand landmarks on the original image for visualization
            drawing_option.draw_landmarks(image, hand)

            # Get the normalized landmark list for one hand
            one_hand_handmarks = hand.landmark

            # Iterate over each landmark point (id and coordinates)
            for id, lm in enumerate(one_hand_handmarks):
                # Convert normalized coordinates to pixel coordinates
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)

                # Index finger tip (landmark id 8) controls mouse cursor position
                if id == 8:
                    # Map the hand position relative to camera frame to screen resolution
                    mouse_x = (screen_width / image_width * x)
                    mouse_y = (screen_height / image_height * y)

                    # Apply smoothing to the mouse movement to avoid jitter
                    prev_mouse_x += (mouse_x - prev_mouse_x) * smoothing_factor
                    prev_mouse_y += (mouse_y - prev_mouse_y) * smoothing_factor

                    # Move the cursor smoothly to the computed position
                    pyautogui.moveTo(prev_mouse_x, prev_mouse_y)

                    # Update fingertip coordinates for drawing line later
                    x1 = x
                    y1 = y

                # Thumb tip (landmark id 4) coordinates for click gesture detection
                if id == 4:
                    x2 = x
                    y2 = y

            # Draw a line between thumb tip and index finger tip to show the gesture
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 2)

        # Calculate vertical distance between thumb tip and index finger tip
        dist = y2 - y1
        print(dist)  # Optional: print distance to console for debugging

        # If the distance is less than a threshold, consider it a "click" gesture
        if dist < 20:
            pyautogui.click()

    # Resize the display window for better visibility (1.5x zoom)
    zoom = 1.5
    resized_image = cv2.resize(image, (int(image_width * zoom), int(image_height * zoom)))

    # Show the webcam feed with hand landmarks and gesture line
    cv2.imshow("Hand movement video capture", resized_image)

    # Wait briefly for a key press; 1 ms for smooth video
    key = cv2.waitKey(1)

    # Exit the loop if 'Esc' key is pressed or window is closed
    if key == 27 or cv2.getWindowProperty("Hand movement video capture", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the webcam and destroy all OpenCV windows on exit
camera.release()
cv2.destroyAllWindows()
