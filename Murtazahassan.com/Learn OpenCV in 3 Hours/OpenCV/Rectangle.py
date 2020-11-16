import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)

pt1 = (10,10)
pt2 = (250,350)
color = (20,20,255)
thickness = 2

cv2.rectangle(img, pt1, pt2, color, thickness)
 
cv2.imshow("Image",img)
cv2.waitKey(0)