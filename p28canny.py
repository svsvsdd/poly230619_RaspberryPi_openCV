import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('timetable.png',0)
edges = cv2.Canny(img,30,200)
edges2 = cv2.Canny(img,100,200)
edges3 = cv2.Canny(img,150,200)

plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image2'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges3,cmap = 'gray')
plt.title('Edge Image3'), plt.xticks([]), plt.yticks([])

plt.show()
