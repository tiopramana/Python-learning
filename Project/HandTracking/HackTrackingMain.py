import cv2
import mediapipe as mp
import time 
import numpy as np

from pathlib import Path


MODEL_PATH = "hand_landmarker_new.task"
CAM_INDEX = 0
DRAW_COLOR = (30, 30, 220)       
DRAW_THICKNESS = 6
ERASE_THICKNESS = 40
SMOOTHING = 0.35 

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17),
]

FINGER_TIPS = {"index": 8, "middle": 12, "ring": 16, "pinky": 20}
FINGER_PIPS = {"index": 6, "middle": 10, "ring": 14, "pinky": 18}

class HandDetector():

    print(mp.__version__)

    def __init__(self, model_path=MODEL_PATH, maxHands=1, detection_confidence=0.6, presence_confidence=0.6, tracking_confidence=0.6):

        model_path = (
            Path(__file__).resolve().parent
            / "hand_landmarker_new.task"
        )

        if not model_path.is_file():
            raise FileNotFoundError(
                f"Model tidak ditemukan: {model_path}"
            )

        model_data = model_path.read_bytes()

        if len(model_data) == 0:
            raise RuntimeError(
                f"File model kosong: {model_path}"
            )

        print("Model ditemukan:", model_path)
        print("Ukuran model:", len(model_data), "bytes")


        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(
                delegate=mp.tasks.BaseOptions.Delegate.CPU,
                model_asset_buffer=model_data
            ),
        running_mode = mp.tasks.vision.RunningMode.VIDEO,
        num_hands = maxHands,
        min_hand_detection_confidence = detection_confidence,
        min_hand_presence_confidence = presence_confidence,
        min_tracking_confidence = tracking_confidence
        )

        self.detector = (mp.tasks.vision.HandLandmarker.create_from_options(options))

        self.results = None
        self.timestamp_ms = 0

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=imgRGB
        )

        current_timestamp = int(time.monotonic() * 1000)

        if current_timestamp <= self.timestamp_ms:
            current_timestamp = self.timestamp_ms + 1

        self.timestamp_ms = current_timestamp

        self.results = self.detector.detect_for_video(
            mp_image,
            self.timestamp_ms
        )

        if draw and self.results.hand_landmarks:
            self.draw_landmarks(img)

        return img


    def draw_landmarks(self, img):

        height, width, _ = img.shape

        for hand_landmarks in self.results.hand_landmarks:
            points = []
            for landmarks in hand_landmarks:
                x = int(landmarks.x * width)
                y = int(landmarks.y * height)

                points.append((x,y))

            for start_index, end_index in HAND_CONNECTIONS:
                cv2.line(
                    img,
                    points[start_index],
                    points[end_index],
                    (0, 255, 0),
                    2
                )

            for x, y in points:
                cv2.circle(
                    img,
                    (x,y),
                    5,
                    (255, 0, 255),
                    cv2.FILLED
                )

    def findPosition(self, img, hand_index=0,):
        land_mark_list = []

        if not self.results:
            return land_mark_list

        if hand_index >= len(self.results.hand_landmarks):
            return land_mark_list

        height, width, _ = img.shape

        handle_marks = self.results.hand_landmarks[hand_index]

        for land_mark_id, landmark in enumerate(handle_marks):
            x = int(landmark.x * width)
            y = int(landmark.y * height)

            land_mark_list.append(
                (
                land_mark_id,
                x,
                y,
                landmark.z
                )
            )

        return land_mark_list

    def close(self):
        self.detector.close   


def fingerUps(points):
    up = {}
    for name in FINGER_TIPS:
        tip_y = points[FINGER_TIPS[name]][1]
        pip_y = points[FINGER_PIPS[name]][1]
        up[name] = tip_y < pip_y
    return up

def classifyGesture(points):
    up = fingerUps(points)

    index, middle, ring, pinky = up["index"], up["middle"], up["ring"], up["pinky"]

    if index and not middle and not ring and not pinky:
        return "draw"
    if index and middle and not ring and not pinky:
        return "erase"
    if index and middle and not ring and pinky:
        return "spawn"


def main():    
    detector = HandDetector(maxHands=1)
    cap = cv2.VideoCapture(CAM_INDEX)


    previous_time = 0

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to open camera!")
            return

        ret, firstFrame = cap.read()
        if not ret:
            print("Failed to read initial frame!")
            return

        height, width = firstFrame.shape[:2]

        canvas = np.ones((height, width, 3), dtype=np.uint8) * 255
        white_board_visual = False

        prev_point = None
        smoothed_point = None

        prev_gesture = None
        spawn_debounce_until = 0.0

        print("Controls:")
        print("  Index finger only      -> Draw")
        print("  Index + Middle (peace) -> Erase")
        print("  Index + Middle + Ring  -> Toggle whiteboard")
        print("  'c' key                -> Clear whiteboard")
        print("  'q' key                -> Quit")

        while True:
            success, frame = cap.read()

            if not success:
                print("Failed to read frame from camera!")
                break

            frame = cv2.flip(frame,1)

            detector.findHands(frame)
            points = detector.findPosition(frame)

            gesture = None
            fingerTip = None

            if points:
                gesture = classifyGesture(points)
                fingerTip = points[FINGER_TIPS["index"]]

                if smoothed_point is None:
                    smoothed_point = fingerTip
                else:
                    sx = int(SMOOTHING * smoothed_point[0] * (1 - SMOOTHING) * fingerTip[0])
                    sy = int(SMOOTHING * smoothed_point[1] + (1 - SMOOTHING) * fingerTip[1])
                    smoothed_point = (sx, sy)

            if gesture == "draw" and smoothed_point:
                if prev_point is not None:
                    cv2.line(canvas, prev_point, smoothed_point, DRAW_COLOR, DRAW_THICKNESS)
                prev_point =  smoothed_point
            elif gesture == "erase" and smoothed_point:
                cv2.circle(canvas, smoothed_point, ERASE_THICKNESS, (255, 255, 255), cv2.FILLED)
                prev_point = None
            elif gesture == "spawn":
                if prev_gesture != "spawn" and now > spawn_debounce_until:


            now = time.time()

    detector.close()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
