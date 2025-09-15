import cv2
import mediapipe
import pyautogui

face_mesh_landmarks=mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam=cv2.VideoCapture(0)
while True:
    _,image=cam.read()
    image=cv2.flip(image,1)
    window_h, window_w, _=image.shape
    rgb_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image=face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points=processed_image.multi_face_landmarks
    print(all_face_landmark_points)
    if all_face_landmark_points:
        one_face_landmark_points=all_face_landmark_points[0].landmark
        for landmark_point in one_face_landmark_points[474:478]:
            x=int(landmark_point.x*window_w)
            y=int(landmark_point.y*window_h)
            print(x,y)
            cv2.circle(image, (x,y), 3, (0,0,255))
        left_eye=[one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x=int(landmark_point.x*window_w)
            y=int(landmark_point.y*window_h)
            print(x,y)
            cv2.circle(image, (x,y), 3, (0,0,255))
    cv2.imshow("Eye controlled mouse", image)
    key=cv2.waitKey(100)
    if key==27:
        break
    if cv2.getWindowProperty("Eye controlled mouse", cv2.WND_PROP_VISIBLE) < 1:
        break
cam.release()
cv2.destroyAllWindows()

    