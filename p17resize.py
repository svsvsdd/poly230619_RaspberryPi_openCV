import cv2
import numpy as np

img = cv2.imread('family.jpg')

res = cv2.resize(img,None, fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)

#height, width = img.shape[:2]
#res = cv2.resize(img,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('origin', img)
cv2.imshow('resizing', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
