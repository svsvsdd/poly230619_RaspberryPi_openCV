import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass
cv2.namedWindow('image')  # 창 생성
cv2.createTrackbar('hsv_scale', 'image', 0, 180, nothing)

while(1):
    ret, frame = cap.read()
    hue = cv2.getTrackbarPos('hsv_scale','image')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([hue-10,0,0])
    upper_blue = np.array([hue+10,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
