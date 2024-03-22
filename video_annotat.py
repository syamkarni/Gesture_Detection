import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 255, 0)
thickness = 2
text = "DETECTED"

def annotate_frame(frm, flag):
    if flag:
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = frm.shape[1] - text_size[0] - 10
        text_y = 30
        cv2.putText(frm, text, (text_x, text_y), font, font_scale, font_color, thickness)
    return frm
