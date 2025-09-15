import cv2
import mediapipe as mp
import pyautogui


x1=y1=x2=y2=0

webcam = cv2.VideoCapture(0)

# Initialize MediaPipe solutions
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _, image = webcam.read()
    if image is None:
        break

    # Get the frame dimensions from the .shape attribute
    frame_height, frame_width, _ = image.shape

    # Flip the image horizontally for a mirror effect and convert to RGB
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image to find hands
    output = hands.process(rgb_image)
    all_hands = output.multi_hand_landmarks

    if all_hands:
        for hand_landmarks in all_hands:
            # Draw landmarks and the connections between them
            drawing_utils.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates for specific landmarks
            for id, landmark in enumerate(hand_landmarks.landmark):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # Draw a circle on the tip of the index finger (landmark 8)
                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1=x
                    y1=y
                # Draw a circle on the tip of the thumb (landmark 4)
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2=x
                    y2=y
    cv2.imshow("Hand Volume Control", image)
    
    key = cv2.waitKey(10)
    if key == 27: # 'ESC' key
        break

webcam.release()
cv2.destroyAllWindows()