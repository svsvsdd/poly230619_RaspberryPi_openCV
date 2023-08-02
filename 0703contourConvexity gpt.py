
import cv2
import numpy as np





# Load the hand image
hand_image = cv2.imread('보.JPG')

# Convert the image to grayscale
gray = cv2.cvtColor(hand_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to extract the hand region
_, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
#contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Find the contour with the largest area (assumed to be the hand)
hand_contour = max(contours, key=cv2.contourArea)

# Convex hull of the hand contour
hand_hull = cv2.convexHull(hand_contour, returnPoints=False)

# Find convexity defects in the hand contour
defects = cv2.convexityDefects(hand_contour, hand_hull)

# Count the number of fingers
num_fingers = 0
for i in range(defects.shape[0]):
    start_idx, end_idx, _, _ = defects[i, 0]
    start_point = tuple(hand_contour[start_idx][0])
    end_point = tuple(hand_contour[end_idx][0])
    far_point = tuple(hand_contour[defects[i, 0, 2]][0])
    
    # Calculate the distance between the farthest point and the line connecting start and end points
    distance = cv2.pointPolygonTest(hand_contour, far_point, True)
    
    # If the distance is larger than a threshold, consider it as a finger
    if distance > 10000:
        num_fingers += 1

# Determine the hand gesture based on the number of fingers
gesture = ''
if num_fingers == 0:
    gesture = 'Rock'
elif num_fingers == 2:
    gesture = 'Scissors'
elif num_fingers == 5:
    gesture = 'Paper'

# Draw the hand contour and defects on the image
cv2.drawContours(hand_image, [hand_contour], 0, (0, 255, 0), 2)
for i in range(defects.shape[0]):
    start_idx, end_idx, farthest_idx, _ = defects[i, 0]
    start_point = tuple(hand_contour[start_idx][0])
    end_point = tuple(hand_contour[end_idx][0])
    farthest_point = tuple(hand_contour[farthest_idx][0])
    cv2.circle(hand_image, farthest_point, 5, (0, 0, 255), -1)

# Display the hand image with the gesture
cv2.putText(hand_image, f'Gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Hand Gesture Recognition', hand_image)
cv2.waitKey(0)
cv2.destroyAllWindows()