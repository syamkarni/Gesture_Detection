import cv2
import mediapipe as mp
import numpy as np

mpose = mp.solutions.pose
pose = mpose.Pose(static_image_mode=False, min_detection_confidence=0.5)

def ext_kp(res):
    kps = []
    if res.pose_landmarks:
        for lm in res.pose_landmarks.landmark:
            kps.append((lm.x, lm.y, lm.z))
    return kps

def proc_frm(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = pose.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    mp.solutions.drawing_utils.draw_landmarks(img, res.pose_landmarks, mpose.POSE_CONNECTIONS)
    return img, res