import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()
face = mp_face.FaceMesh()

cap = cv2.VideoCapture(0)

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

video_playing = False

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Gagal baca frame kamera, skip...")
        continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_result = hands.process(rgb)
    face_result = face.process(rgb)

    if hand_result.multi_hand_landmarks and face_result.multi_face_landmarks:
                for hand_landmarks in hand_result.multi_hand_landmarks:
                    mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,                   # draws finger lines
                        mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),   # red dots
                        mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2)                 # white lines
                    )

                for face_landmarks in face_result.multi_face_landmarks:
                    mp_draw.draw_landmarks(
                        frame,
                        face_landmarks,
                        mp_face.FACEMESH_CONTOURS,
                        mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
                    )

                # Calculate distance between hand and mouth
                for hand_landmarks in hand_result.multi_hand_landmarks:
                    hand_point = hand_landmarks.landmark[0]
                    # Get mouth point from face landmarks (landmark 13 is near mouth area)
                    face_landmarks = face_result.multi_face_landmarks[0]
                    mouth_point = face_landmarks.landmark[13]
                    
                    dist = distance(hand_point, mouth_point)

                    if dist < 0.8:
                        if not video_playing:
                            print("Mulut tertutup tangan! PLAY VIDEO")
                            video_playing = True

                            video = cv2.VideoCapture("video.mp4")
                            if not video.isOpened():
                                print("ERROR: video.mp4 tidak ditemukan!")
                            else:
                                while video.isOpened():
                                    ret_v, frame_v = video.read()
                                    if not ret_v:
                                        break
                                    cv2.imshow("VIDEO", frame_v)
                                    if cv2.waitKey(25) & 0xFF == ord('q'):
                                        break
                                video.release()
                                cv2.destroyWindow("VIDEO")

                            video_playing = False

    cv2.imshow("CAM", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()