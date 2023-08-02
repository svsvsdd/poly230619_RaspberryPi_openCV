import cv2
import numpy as np
from shapely.geometry import Polygon
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower = np.array([0,40,80])
    upper = np.array([20,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.blur(mask, (5,5))
    #contours, hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_areas = [cv2.contourArea(cnt) for cnt in contours]
    max_contour_index = np.argmax(contour_areas)
    max_contour = contours[max_contour_index]
    cv2.drawContours(frame, [max_contour], -1, (0,255,0), 2)
    #max_contour2 = np.squeeze(max_contour)
    #polygon = Polygon(max_contour2)
    #if polygon.is_simple==False:
     #   None
    #elif polygon.is_simple==True:
    count = 0
    text = None
    hull = cv2.convexHull(max_contour, returnPoints = False)
    defects = cv2.convexityDefects(max_contour, hull)
    if defects is not None:
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(max_contour[s][0])
            end = tuple(max_contour[e][0])
            far = tuple(max_contour[f][0])
            cv2.line(frame,start,end,[255,0,0],2)
            cv2.circle(frame,far,5,[0,0,255],-1)
            if d > 16000:
                count = count + 1
    if count > 3:
        text = "paper"
        count = 0
    elif count == 1:
        text = "scissors"
        count = 0
    elif count == 0:
        text = "rock"
        count = 0
    if text != None:
        cv2.putText(frame, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()