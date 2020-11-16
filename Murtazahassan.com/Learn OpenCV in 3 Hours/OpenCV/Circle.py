import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)
center = (200,100)
radius = 25
color = (255,100,100)
thickness = 2
cv2.circle(img, center, radius, color, thickness)
 
cv2.imshow("Image",img)
cv2.waitKey(0)