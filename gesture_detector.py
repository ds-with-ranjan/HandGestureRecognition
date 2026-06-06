import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self, mode=False, max_hands=1, detection_con=0.7, track_con=0.7):
        """
        Initializes the MediaPipe Hands model.
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20] # Landmarks for finger tips

    def find_hands(self, img, draw=True):
        """
        Detects hands in the frame and optionally draws landmarks.
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0):
        """
        Returns a list of landmark coordinates for the detected hand.
        """
        self.lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lm_list.append([id, cx, cy])
        return self.lm_list

    def count_fingers(self):
        """
        Determines how many fingers are currently raised.
        Returns an integer (0-5).
        """
        fingers = []
        if len(self.lm_list) != 0:
            # Thumb: Check x-coordinates (assuming Right Hand for baseline)
            # If the tip is further right/left than the lower joint
            if self.lm_list[self.tip_ids[0]][1] > self.lm_list[self.tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers: Check y-coordinates (tip vs lower joint)
            for id in range(1, 5):
                if self.lm_list[self.tip_ids[id]][2] < self.lm_list[self.tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            return fingers.count(1)
        return 0