import cv2
import mediapipe as mp
import math
import winsound
import time

# --- Constants for easy tuning ---
WINDOW_NAME = "AI Selfie Camera"
# CORRECT landmark IDs for the left and right corners of the mouth
LEFT_CORNER_ID = 61
RIGHT_CORNER_ID = 291
# Adjust this threshold based on your camera and how wide you want the smile to be
SMILE_THRESHOLD = 70

# --- Initialization ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
camera = cv2.VideoCapture(0)
# --- Main Loop ---
while True:
    # Check if the user has closed the window with the 'X' button
    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break
    success, image = camera.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    # Flip the image for a mirror view
    image = cv2.flip(image, 1)
    fh, fw, _ = image.shape
    # Process the image with MediaPipe
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_image)
    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark
        # Initialize coordinates for the mouth corners for this frame
        x1, y1 = 0, 0  # Right mouth corner
        x2, y2 = 0, 0  # Left mouth corner
        # Loop through landmarks to find the corners of the mouth
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)
            # Find the right corner of the mouth (from viewer's perspective)
            if id == RIGHT_CORNER_ID:
                x1, y1 = x, y
                cv2.circle(image, (x, y), 5, (0, 255, 255), -1)
            # Find the left corner of the mouth
            if id == LEFT_CORNER_ID:
                x2, y2 = x, y
                cv2.circle(image, (x, y), 5, (0, 255, 255), -1)
        # Proceed only if both mouth corners were successfully detected
        if x1 and y1 and x2 and y2:
            # Draw a line between the corners for visual feedback
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)    
            # Calculate the distance ONCE using the correct formula
            distance = math.hypot(x2 - x1, y2 - y1)
            cv2.putText(image, f"Smile Width: {distance:.0f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Check if the smile width meets the threshold to take a selfie
            if distance > SMILE_THRESHOLD:
                cv2.putText(image, "SMILE! Taking selfie...", (fw // 4, fh // 2), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)         
                winsound.Beep(1200, 200) # Beep to signal a photo            
                filename = f"selfie_{int(time.time())}.png"
                cv2.imwrite(filename, image)
                print(f"Selfie saved as {filename}!")            
                # Stop the program after taking one picture
                break
    # Display the final image in a named window
    cv2.imshow(WINDOW_NAME, image)
    # Exit loop if 'ESC' key is pressed
    if cv2.waitKey(10) == 27:
        break
# --- Cleanup ---
camera.release()
cv2.destroyAllWindows()