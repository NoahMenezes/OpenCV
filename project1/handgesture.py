import cv2
import mediapipe
import pyautogui

# Initialize Mediapipe Hands solution
capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Start webcam
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0

# Cursor smoothing
prev_mouse_x = 0
prev_mouse_y = 0
smoothing_factor = 0.2

while True:
    _, image = camera.read()
    image_height, image_width, _ = image.shape
    image = cv2.flip(image, 1)  # Mirror the image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process image to detect hands
    output_hands = capture_hands.process(rgb_image)

    # Corrected attribute name here
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        for hand in all_hands:
            # Draw hand landmarks on the image
            drawing_option.draw_landmarks(image, hand)
            one_hand_handmarks = hand.landmark
            for id, lm in enumerate(one_hand_handmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)

                if id == 8:
                    mouse_x = (screen_width / image_width * x)
                    mouse_y = (screen_height / image_height * y)

                    # Smooth movement
                    prev_mouse_x += (mouse_x - prev_mouse_x) * smoothing_factor
                    prev_mouse_y += (mouse_y - prev_mouse_y) * smoothing_factor
                    pyautogui.moveTo(prev_mouse_x, prev_mouse_y)

                    # No dot drawn
                    x1 = x
                    y1 = y

                if id == 4:
                    x2 = x
                    y2 = y
                    # No dot drawn

            # Draw a line connecting thumb tip and index finger tip
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 2)

        dist = y2 - y1
        print(dist)
        if dist < 20:
            pyautogui.click()

    # Show the webcam feed with drawings
    cv2.imshow("Hand movement video capture", image)

    key = cv2.waitKey(1)  # More responsive
    if key == 27:
        break
    if cv2.getWindowProperty("Hand movement video capture", cv2.WND_PROP_VISIBLE) < 1:
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()
