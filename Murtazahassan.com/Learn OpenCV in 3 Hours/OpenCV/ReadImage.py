import cv2
# Load an image
img = cv2.imread("Resources/lena.png")
# Display an image
title = "Lena Soderberg"
cv2.imshow(title, img)
cv2.waitKey(0)