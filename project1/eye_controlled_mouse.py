import cv2
import mediapipe
import pyautogui
import time

# Initialize Face Mesh detector with landmark refinement enabled (for better eye detection)
face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Start the webcam
cam = cv2.VideoCapture(0)

# Get screen dimensions (used for mapping face landmarks to screen coordinates)
screen_w, screen_h = pyautogui.size()

# Variable to manage delay between mouse clicks (cooldown)
click_cooldown = 0

while True:
    # Capture frame from webcam
    _, image = cam.read()

    # Flip image horizontally for natural interaction (mirror effect)
    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape

    # Convert the image to RGB format for Mediapipe processing
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run Face Mesh detection
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks

    # If any faces are detected
    if all_face_landmark_points:
        # Use the first detected face
        one_face_landmark_points = all_face_landmark_points[0].landmark

        # Track iris landmarks (474 to 477) – used to control cursor
        for i, landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)

            if i == 1:
                # Convert coordinates from camera space to screen space
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)

                # Move the mouse cursor to calculated position
                pyautogui.moveTo(mouse_x, mouse_y, duration=0.05)

            # Draw red circles around iris landmarks for visual feedback
            cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

        # Track two specific left eye landmarks for blink detection
        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]

        for point in left_eye:
            x = int(point.x * window_w)
            y = int(point.y * window_h)
            # Draw yellow circles on the eyelid points
            cv2.circle(image, (x, y), 4, (0, 255, 255), -1)

        # Calculate vertical distance between eyelids to detect blink
        blink_ratio = abs(left_eye[0].y - left_eye[1].y)

        # If eye is "closed" and 1 second has passed since last click
        if blink_ratio < 0.012 and time.time() - click_cooldown > 1:
            pyautogui.click()
            click_cooldown = time.time()
            print("mouse clicked")

    # Scale up the image display for better user experience
    zoom = 1.3
    resized = cv2.resize(image, (int(window_w * zoom), int(window_h * zoom)))

    # Show the resized window
    cv2.imshow("Eye Controlled Mouse", resized)

    # Exit on ESC key or if window is manually closed
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty("Eye Controlled Mouse", cv2.WND_PROP_VISIBLE) < 1:
        break

# Cleanup: release webcam and destroy all OpenCV windows
cam.release()
cv2.destroyAllWindows()
