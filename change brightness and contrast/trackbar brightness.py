import numpy as np
import cv2

# cap = cv2.VideoCapture("K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\thamkhao\\video\\N.mp4")
cap = cv2.VideoCapture(0)
brightness = 50

# create trackbar with white background
trackbars_img = np.uint8(np.full((50, 500, 3), 255))
cv2.imshow('trackbars', trackbars_img)


def brightness_change(x):
    global brightness
    brightness = x


# create trackbar (trackbar name, window name, default value, max value, onChange)
cv2.createTrackbar('Brightness', 'trackbars', 50, 100, brightness_change)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    brightness_adjuster = int((brightness - 50) / 50 * 255)
    # print(brightness_adjuster)

    v_int16 = np.int16(v) + brightness_adjuster
    v_int16[v_int16 > 255] = 255
    v_int16[v_int16 < 0] = 0
    # print(v_int16)
    #
    # brightness_adjuster = int((brightness - 50))
    #
    # v = cv2.add(v, brightness_adjuster)
    # v[v > 255] = 255
    # v[v < 0] = 0

    v = np.uint8(v_int16)
    # print(v)
    final_hsv = cv2.merge((h, s, v))

    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

    if cv2.waitKey(1) == ord('p'):
        # wait until any key is pressed
        cv2.waitKey(-1)

cap.release()
cv2.destroyAllWindows()
