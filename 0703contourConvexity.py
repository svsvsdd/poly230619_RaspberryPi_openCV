#Filename : Convexity.py  star.jpg  보.JPG   가위

import cv2
import numpy as np

img = cv2.imread('가위.JPG')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 230,255,1) 
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# original contour를 얻은 후 그린다.
cv2.drawContours(img, contours, -1, (0,255,0), 2)
cnt = contours[0]
 
# convex hull을 얻는다.
hull = cv2.convexHull(cnt,returnPoints = False)
# convexity defects를 구한다.
defects = cv2.convexityDefects(cnt,hull)


for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end,[255,0,0], 2)
    cv2.circle(img, far, 5, [0,0,255], -1)
 
min_defect_length = 10000

num_defects = defects.shape[0]

# 판단 기준을 변경하여 제스처를 판단
if defects[:, 0, 3].min() > min_defect_length:

    if num_defects == 0:
        gesture = 'Rock'
    elif num_defects == 5:
        gesture = 'Scissors'
    elif num_defects == 4:
        gesture = 'Paper'
    elif num_defects == 6:
        gesture = '6'    
    else:
        gesture = 'Unknown'

else:
    gesture = 'Unknown'       
cv2.imshow('img',img)
print(gesture)

cv2.waitKey(0)
cv2.destroyAllWindows()