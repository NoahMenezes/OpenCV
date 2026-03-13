import csv
from pyzbar.pyzbar import decode
from PIL import Image 
import cv2
# im
CSV_FILE_NAME = "SmartAttendance.csv"
WINDOW_NAME = "Attendance System"
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not open video stream.")
    exit()
students = []
try:
    with open(CSV_FILE_NAME, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                 students.append(row[1])

    print(f"Loaded {len(students)} students from {CSV_FILE_NAME}")

except FileNotFoundError:
    print(f"Error: The file '{CSV_FILE_NAME}' was not found.")
    exit()


while True:
    check, frame = video.read()
    if not check:
        print("Error: Failed to capture image.")
        break
    
    decoded_objects = decode(frame)
    
    if decoded_objects:
        name_bytes = decoded_objects[0].data
        name = name_bytes.decode('utf-8')

        if name in students:
            students.remove(name)
            print(f"ATTENDANCE TAKEN: {name}. Students remaining: {len(students)}")
            
            (x, y, w, h) = decoded_objects[0].rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "ATTENDED", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        else:
            (x, y, w, h) = decoded_objects[0].rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "NOT FOUND/DUPLICATE", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    cv2.imshow(WINDOW_NAME, frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("\n--- Attendance Summary ---")
        print("Students NOT checked in:")
        for student in students:
             print(f"- {student}")
        break

video.release()
cv2.destroyAllWindows()




# incomplete -> video https://www.youtube.com/watch?v=o9-cY0R7VME&list=PL288dDBJtFXAsIohAOBShGe8NLqJ9Zwsk&index=4