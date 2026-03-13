import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize hands module and drawing utils
from mediapipe.python.solutions import hands as mp_hands_module
from mediapipe.python.solutions import drawing_utils as mp_drawing

hands = mp_hands_module.Hands(max_num_hands=1, model_complexity=1)
drawing_utils = mp_drawing

x1 = y1 = x2 = y2 = 0
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand_landmarks)

            for id, lm in enumerate(hand_landmarks.landmark):
                x = int(lm.x * w)
                y = int(lm.y * h)

                if id == 8:
                    cv2.circle(frame, (x, y), 8, (0, 255, 255), 3)
                    x1, y1 = x, y
                if id == 4:
                    cv2.circle(frame, (x, y), 8, (0, 0, 255), 3)
                    x2, y2 = x, y

            dist = math.hypot(x2 - x1, y2 - y1)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            if dist > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

    cv2.imshow("Hand Volume Control", frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()