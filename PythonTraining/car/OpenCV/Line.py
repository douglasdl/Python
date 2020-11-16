import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)

p1 = (0,0)
p2 = (img.shape[1],img.shape[0])
color = (0,255,0)
thickness = 3
cv2.line(img, p1, p2, color, thickness)
 
cv2.imshow("Image",img)
cv2.waitKey(0)