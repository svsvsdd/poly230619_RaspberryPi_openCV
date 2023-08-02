import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.jpg')

kernel = np.ones((9,9),np.float32)/81
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(211),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()