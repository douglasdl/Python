import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)

text = "Hello Image"
org = (100,200)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
color = (0,150,0)
thickness = 1
cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
 
cv2.imshow("Image",img)
cv2.waitKey(0)