import cv2
import mediapipe
import pyautogui
import time

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
click_cooldown = 0

while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks

    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark
        for i, landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            if i == 1:
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)
                pyautogui.moveTo(mouse_x, mouse_y, duration=0.05)
            cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        for point in left_eye:
            x = int(point.x * window_w)
            y = int(point.y * window_h)
            cv2.circle(image, (x, y), 4, (0, 255, 255), -1)

        blink_ratio = abs(left_eye[0].y - left_eye[1].y)
        if blink_ratio < 0.012 and time.time() - click_cooldown > 1:
            pyautogui.click()
            click_cooldown = time.time()
            print("mouse clicked")

    zoom = 1.3
    resized = cv2.resize(image, (int(window_w * zoom), int(window_h * zoom)))
    cv2.imshow("Eye Controlled Mouse", resized)

    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty("Eye Controlled Mouse", cv2.WND_PROP_VISIBLE) < 1:
        break

cam.release()
cv2.destroyAllWindows()
