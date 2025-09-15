import cv2
import winsound

# Open webcam
webcam = cv2.VideoCapture(0)
_, im1 = webcam.read()
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

motion_counter = 0  # Initialize counter

while True:
    _, im2 = webcam.read()
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(im1, im2_gray)
    _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected_this_frame = False

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        if not motion_detected_this_frame:
            motion_counter += 1
            print(f"Motion detected! Count: {motion_counter}")
            winsound.Beep(500, 100)
            motion_detected_this_frame = True  # Avoid multiple increments in one frame
    # Put the counter text on the image
    cv2.putText(
        diff,                            # image to draw on
        f"Motion Count: {motion_counter}",  # text
        (10, 30),                       # bottom-left corner of text
        cv2.FONT_HERSHEY_SIMPLEX,       # font
        1,                             # font scale
        (255, 255, 255),               # color (white)
        2                              # thickness
    )

    cv2.imshow("Security camera", diff)
    im1 = im2_gray.copy()

    if cv2.waitKey(10) == 27:
        break
    if cv2.getWindowProperty("Security camera", cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv2.destroyAllWindows()
