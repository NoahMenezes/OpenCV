import cv2
import os
CASCADE_PATH = 'haarcascade_frontalface_default.xml'
WINDOW_NAME = "Face Detection"

if not os.path.exists(CASCADE_PATH):
    print(f"Error: Cascade file not found at '{CASCADE_PATH}'")
    exit()
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
if face_cascade.empty():
    print("Error: Could not load cascade classifier.")
    exit()
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()
print("Starting webcam... Press 'ESC' to exit.")

while True:
    # Read a frame from the webcam
    ret, frame = webcam.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    # Convert the frame to grayscale for the face detector
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow(WINDOW_NAME, frame)
     # --- Exit Conditions ---
    # Wait for a key press for 1ms
    key = cv2.waitKey(1)
    # 1. Break if 'ESC' key is pressed
    if key == 27:
        break
    # 2. Break if the window's 'X' button is clicked
    # This checks if the window is still visible. If not, it breaks the loop.
    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break
print("Closing application...")
webcam.release()
cv2.destroyAllWindows()