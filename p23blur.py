import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.jpg')

blur = cv2.blur(img,(5,5))

plt.subplot(211),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
