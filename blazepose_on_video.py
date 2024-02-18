import cv2
import time
import mediapipe as mp
from annotations_input import read_csv_file, get_time
from annotations_output import write_key

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

avg = 0
count = 0

annotations = read_csv_file('1.csv')

cap = cv2.VideoCapture("d3.mp4")

with mp_pose.Pose(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("no video in frame")
            break

        frame_time = cap.get(0)/1000
        activity = get_time(annotations, frame_time)
        print(frame_time, "   ", activity)

        start_time = time.time()
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (500, 700))
        result = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(
            image,
            result.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

        # Write key points to csv file
        # write_key(result, frame_time, activity)

        # Displays the result to the Screen
        cv2.imshow('media pipe pose', cv2.flip(image, 1))

        # Calculate the Average fps of the model
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        avg += fps
        count += 1

        if cv2.waitKey(5) & 0xFF == 27:
            break

print("average fps is ", avg / count)
cap.release()
