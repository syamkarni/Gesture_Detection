import cv2


def annotate_frame(frm, flag):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (0, 255, 0)
    bg_color= (0, 0, 0)
    thickness = 3
    text = "DETECTED"
    if flag:
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int(frm.shape[1] - text_size[0] - 10)
        text_y = int(text_size[1] + 10)
        cv2.rectangle(frm, (text_x, text_y - text_size[1] - 10), (text_x + text_size[0], text_y + 10), bg_color, -1)
        cv2.putText(frm, text, (text_x, text_y), font, font_scale, font_color, thickness)
    return frm
