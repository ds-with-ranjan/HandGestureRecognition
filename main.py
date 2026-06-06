import cv2
import time
from gesture_detector import GestureDetector
from actions import ActionController

def main():
    # 1. Initialize Camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280) # Width
    cap.set(4, 720)  # Height

    # 2. Initialize Modules
    detector = GestureDetector(max_hands=1, detection_con=0.8)
    controller = ActionController(cooldown=3.0) # 3-second delay between actions

    print("System Started. Press 'q' to quit.")

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame from camera. Exiting...")
            break

        # Flip image horizontally for a selfie-view display
        img = cv2.flip(img, 1)

        # 3. Detect Hands and Count Fingers
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)
        
        fingers = 0
        action_text = "Action: None"

        if len(lm_list) != 0:
            fingers = detector.count_fingers()
            
            # 4. Perform Action Based on Finger Count
            # We only trigger if 0, 1, 2, 3, or 4 fingers are showing. 
            # 5 fingers is considered a neutral/idle state for this application.
            if fingers in [0, 1, 2, 3, 4]:
                action_text = controller.perform_action(fingers)
            else:
                action_text = "Idle (5 Fingers)"

        # 5. UI / On-Screen Display
        # Display Finger Count
        cv2.rectangle(img, (20, 20), (170, 160), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(fingers), (60, 120), cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 10)
        
        # Display Cooldown / Current Action Status
        cv2.putText(img, action_text, (200, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # 6. Show the frame
        cv2.imshow("Hand Gesture Recognition System", img)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()