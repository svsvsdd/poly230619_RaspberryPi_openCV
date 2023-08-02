#Filename : convex.py

import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()


    # = cv2.imread('보.JPG')
    img1 = img.copy()
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 230,255,1)
    image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
    cv2.imshow('Original Contour', img)
    #cv2.imshow('imgray Contour', imgray)
    # contour가 Convex Hull 인지를 확인한다.
    chk = cv2.isContourConvex(cnt)

    if not chk:
       cvxhull = cv2.convexHull(cnt)
       cv2.drawContours(img1, [cvxhull], 0, (0, 255, 0), 3)
       cv2.imshow('Convex Hull', img1)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

