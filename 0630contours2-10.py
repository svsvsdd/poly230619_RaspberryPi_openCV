import cv2 
import numpy as np 

img = cv2.imread('POLY.jpg') 
img1 = img.copy()

img2 = img.copy() 

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(imgray, 120,255,0) 
 
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE) 
 
# 첫 번째 contour에 대한 모멘트 정보를 출력한다.
mom = contours[2] 
M = cv2.moments(mom)

epsilon1 = 0.05 * cv2.arcLength(mom, True)
epsilon2 = 0.08 * cv2.arcLength(mom, True)
approx1 = cv2.approxPolyDP(mom, epsilon1, True)
approx2 = cv2.approxPolyDP(mom, epsilon2, True)

cv2.drawContours(img, [mom], 0, (0, 255, 0), 3)
cv2.drawContours(img1, [approx1], 0, (255, 0, 0), 3)
cv2.drawContours(img2, [approx2], 0, (0, 0, 255), 3)

cv2.imshow('Origin', img)
cv2.imshow('approx1', img1)
cv2.imshow('approx2', img2)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
