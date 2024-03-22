import cv2
from main import proc_frm, ext_kp
from gesture_sim import sim
from video_annotat import annotate_frame

inp_img = cv2.imread('test.jpg')
if inp_img is None:
    raise ValueError("The image failed to load. Check the file path and file integrity.")
proc_img, inp_res = proc_frm(inp_img)
inp_kp = ext_kp(inp_res)

cap = cv2.VideoCapture('video.mp4')

my_thrsh = 0.05

while cap.isOpened():
    ret, frm = cap.read()
    if not ret:
        break

    p_frm, frm_res = proc_frm(frm)
    frm_kp = ext_kp(frm_res)

    s = sim(inp_kp, frm_kp)
    detect_flag = s < my_thrsh

    p_frm = annotate_frame(p_frm, detect_flag)
    cv2.imshow('Detection', p_frm)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
