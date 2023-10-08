"""
This program implements the Wisconsin Autonomous perception coding challenging by using OpenCV to detect the boundaries
defined by cones in the given image.

Implemented by Sandeep Sankar (email: sankar5@wisc.edu)
"""

import numpy as np
import cv2

# Importing the image
img = cv2.imread("assets/red.png")
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# Converting to an HSV color frame
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_color = np.array([0, 158, 158])
upper_color = np.array([30, 255, 255])

# Creating a binary mask of the image
mask = cv2.inRange(hsv, lower_color, upper_color)

# Finding the contours in the mask and drawing them on a copy
answer_image = img.copy()
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

# Separate contours into left and right based on x-coordinate
left_contours = []
right_contours = []

for contour in contours:
    x, _, _, _ = cv2.boundingRect(contour)

    if x <= 400: # x = 400 separates the left and right contours
        left_contours.append(contour)
    else:
        right_contours.append(contour)

left_arr = np.vstack(left_contours)
right_arr = np.vstack(right_contours)

# Drawing left line
[left_vx, left_vy, left_x0, left_y0] = cv2.fitLine(left_arr, cv2.DIST_L2, 0, 0.01, 0.01)
left_x0, left_y0, left_vx, left_vy = left_x0[0], left_y0[0], left_vx[0], left_vy[0]

line_length = 1000

# Calculating the start and end points for the line
left_x1 = int(left_x0 - line_length * left_vx)
left_y1 = int(left_y0 - line_length * left_vy)
left_x2 = int(left_x0 + line_length * left_vx)
left_y2 = int(left_y0 + line_length * left_vy)

cv2.line(answer_image, (left_x1, left_y1), (left_x2, left_y2), (0, 0, 255), 2)

# Drawing right line
[right_vx, right_vy, right_x0, right_y0] = cv2.fitLine(right_arr, cv2.DIST_L2, 0, 0.01, 0.01)
right_x0, right_y0, right_vx, right_vy = right_x0[0], right_y0[0], right_vx[0], right_vy[0]

# Calculating the start and end points for the line
right_x1 = int(right_x0 - line_length * right_vx)
right_y1 = int(right_y0 - line_length * right_vy)
right_x2 = int(right_x0 + line_length * right_vx)
right_y2 = int(right_y0 + line_length * right_vy)

cv2.line(answer_image, (right_x1, right_y1), (right_x2, right_y2), (0, 0, 255), 2)

# Saving the image with boundaries
cv2.imwrite("answer.png", answer_image)

# Displaying the image with boundaries
cv2.imshow("Image", answer_image)
cv2.waitKey(0)
cv2.destroyAllWindows()