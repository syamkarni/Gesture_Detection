import cv2

def annotate_frame(frm, flag):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)
    thickness = 4
    text = "DETECTED"
    margin = 10
    
    if flag:
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = frm.shape[1] - text_size[0] - margin
        text_y = text_size[1] + margin 
        cv2.putText(frm, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    return frm

if __name__ == "__main__":
    frm = cv2.imread("test.jpg")
    frm = annotate_frame(frm, True)

    cv2.imshow("window", frm)
    cv2.waitKey(0)