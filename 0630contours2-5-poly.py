#Filename : approx.py 

import numpy as np 
import cv2

img = cv2.imread('POLY.jpg') 
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(imgray,120,255, cv2.THRESH_BINARY_INV) 
# 이미지에서 contour를 탐색한다
image1, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

mom = contours[5] 
# 탐색된 contour를 원본 이미지에 그린다
#cv2.drawContours(img1, [mom], 0, (0,0,255), 1) 

for point in mom:
    x, y = point[0]
    cv2.circle(img1, (x, y), 3, (0, 0, 255), -1)

cv2.imshow('APPROX_SIMPLE', img1) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

