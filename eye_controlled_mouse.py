import cv2
import mediapipe
import pyautogui

face_mesh_landmarks=mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam=cv2.VideoCapture(0)



cam=cv2.VideoCapture(0)
while True:
    _,image=cam.read()
    cv2.imshow("Eye controlled mouse", image)
    key=cv2.waitKey(100)
    if key==27:
        break
    
cam.release()
cv2.destroyAllWindows()

    