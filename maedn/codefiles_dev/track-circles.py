import cv2
import numpy as np

image = cv2.imread('boardforshow.png')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 80)

if circles is not None:
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)

cv2.imshow("circle",output)
cv2.waitKey(0)