import cv2
import numpy as np
  
img = cv2.imread('Resources/lena.png')
imgVer = np.vstack((img,img))
cv2.imshow("Vertical",imgVer)
 
cv2.waitKey(0)