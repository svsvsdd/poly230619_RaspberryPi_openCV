#Filename : moment.py 

import cv2 
import numpy as np 

img = cv2.imread('family.jpg') 
img1 = img.copy() 
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(imgray, 120,255,0) 
 
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE) 
 
# 첫 번째 contour에 대한 모멘트 정보를 출력한다.
mom = contours[0] 
M = cv2.moments(mom) 

print(M)

cv2.imshow('moment', image) 

cx = int(M['m10']/M['m00']) 
cy = int(M['m01']/M['m00']) 

print('cx : ', cx) 
print('cy : ', cy)

cv2.waitKey(0) 
cv2.destroyAllWindows() 