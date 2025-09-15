import cv2
import mediapipe as mp
import math

# --- Constants ---
# Landmark IDs for the left and right corners of the mouth
LEFT_CORNER_ID = 61
RIGHT_CORNER_ID = 291
# You may need to adjust this threshold based on your camera and distance
SMILE_THRESHOLD = 70 

# --- Initialization ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)

# --- Main Loop ---
while True:
    success, image = camera.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image for a "mirror" view
    image = cv2.flip(image, 1)
    
    # Get image dimensions
    fh, fw, _ = image.shape
    
    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and find face landmarks
    output = face_mesh.process(rgb_image)
    landmark_points = output.multi_face_landmarks

    if landmark_points:
        # Get landmarks of the first face found
        landmarks = landmark_points[0].landmark
        
        # Initialize coordinates for mouth corners for the current frame
        x1, y1 = 0, 0 # Right corner
        x2, y2 = 0, 0 # Left corner

        # Iterate through landmarks to find the mouth corners
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)

            # Get coordinates of the right corner of the mouth
            if id == RIGHT_CORNER_ID:
                x1, y1 = x, y
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

            # Get coordinates of the left corner of the mouth
            if id == LEFT_CORNER_ID:
                x2, y2 = x, y
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

        # Check if both mouth corners were detected
        if x1 and y1 and x2 and y2:
            # Draw a line between the mouth corners
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Calculate the Euclidean distance between the corners
            dist = math.hypot(x2 - x1, y2 - y1)
            
            # Display the distance on the screen
            cv2.putText(image, f"Distance: {dist:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Check if the distance exceeds the smile threshold
            if dist > SMILE_THRESHOLD:
                # Only display the text, no selfie is taken
                cv2.putText(image, "SMILE DETECTED!", (fw // 4, fh // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    # Display the output
    cv2.imshow("Smile Detector", image)
    
    # Exit loop if 'ESC' key is pressed
    key = cv2.waitKey(10)
    if key == 27:
        break

# --- Cleanup ---
camera.release()
cv2.destroyAllWindows()