import cv2


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


img = cv2.imread('K:\\PROJECT\\QT\\QT_APP_1\\APP\\Project\\picture\\anh_tb.png')
img2 = increase_brightness(img, 100)

cv2.imshow('Anh goc', img)
cv2.imshow('Anh sang', img2)

cv2.waitKey()
cv2.destroyAllWindows()
