import cv2
import numpy as np

img = cv2.imread('logo.jpg')
b,g,r = cv2.split(img)
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
img = cv2.merge((r,g,b))


cv2.waitKey(0)
cv2.destroyAllWindows()


