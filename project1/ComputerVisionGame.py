import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
import random

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
HandLandmark = mp_hands.HandLandmark

# Game variables
score = 0
# Initial enemy position will be updated later based on frame size
x_enemy = 0
y_enemy = 0
WINDOW_NAME = "Hand Tracking Game" 

# --- CONFIGURATION FOR QUALITY AND SIZE ---
# Recommended for a good balance of size and performance
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FRAME_FPS = 30
# ------------------------------------------

def draw_enemy(image):
    """Draw the enemy circle on the image"""
    # Uses the globally defined x_enemy and y_enemy
    cv2.circle(image, (x_enemy, y_enemy), 25, (0, 200, 0), 5)
    return image

def update_score(image):
    """Update and display the score on the image"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 0, 255) # Magenta
    image = cv2.putText(image, f"Score: {score}", (10, 30), font, 1, color, 2, cv2.LINE_AA)
    return image

def reset_enemy_position(w, h):
    """Helper function to place enemy randomly within frame bounds."""
    global x_enemy, y_enemy
    # Ensure enemy is at least 50 pixels from the edge
    x_enemy = random.randint(50, w - 50) 
    y_enemy = random.randint(50, h - 50)

def main():
    global score, x_enemy, y_enemy
    
    # Initialize video capture
    video = cv2.VideoCapture(0)
    
    # --- APPLY SCREEN SIZE AND QUALITY SETTINGS ---
    video.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    video.set(cv2.CAP_PROP_FPS, FRAME_FPS)
    # ----------------------------------------------
    
    # Get the actual dimensions the camera provided (might differ from requested)
    actual_w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Initialize enemy position based on actual frame size
    reset_enemy_position(actual_w, actual_h)
    
    print(f"Game starting at Resolution: {actual_w}x{actual_h}")

    # Initialize MediaPipe Hands
    with mp_hands.Hands(
        min_detection_confidence=0.8,
        min_tracking_confidence=0.5) as hands:
        
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
                
            # Flip the frame horizontally for a later selfie-view display
            image = cv2.flip(frame, 1)
            
            # Get current frame dimensions
            h, w, _ = image.shape 
            
            # Convert the BGR image to RGB for MediaPipe
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Process the image and detect hands
            results = hands.process(rgb_image)
            
            # Draw the enemy
            image = draw_enemy(image)
            
            # Update and display score
            image = update_score(image)
            
            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4), # Point color
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2) # Line color
                    )
                    
                    # Get index finger tip coordinates (Landmark 8)
                    index_tip = hand_landmarks.landmark[HandLandmark.INDEX_FINGER_TIP]
                    x, y = int(index_tip.x * w), int(index_tip.y * h)
                    
                    # Draw circle at index finger tip (cursor)
                    cv2.circle(image, (x, y), 10, (0, 255, 0), -1)
                    
                    # Check collision with enemy
                    # Collision distance is 35 (25 enemy radius + 10 finger radius)
                    distance = ((x - x_enemy) ** 2 + (y - y_enemy) ** 2) ** 0.5
                    if distance < 35:  
                        reset_enemy_position(w, h)
                        score += 1
            
            # Display the image
            cv2.imshow(WINDOW_NAME, image)
            
            # Break the loop if 'q' is pressed or the window is closed
            key = cv2.waitKey(10) & 0xFF
            if key == ord('q'):
                break
            
            if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
                break
                
    # Release resources
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()