import cv2
import mediapipe as mp
import pyautogui
import winsound
x1=0
y1=0
x2=0
y2=0

face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera=cv2.VideoCapture(0)
while True:
    _, image=camera.read()
    image=cv2.flip(image,1)
    fh, fw, _=image.shape
    rgb_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_image)
    landmark_points=output.multi_face_landmarks
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x=int(landmark.x*fw)
            y=int(landmark.y*fh)
            if id == 43:
                x1=x
                y1=y
            if id == 43:
                x2=x
                y2=y
    cv2.imshow("Auto selfie for smiling faces using python", image)
    key=cv2.waitKey(100)
    if key==27:
        break
camera.release()
cv2.destroyAllWindows()
