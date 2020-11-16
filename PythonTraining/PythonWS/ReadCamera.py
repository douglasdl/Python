import cv2

frameWidth = 640
frameHeight = 480
frameBrightness = 100

cap = cv2.VideoCapture()
cap.set(3, frameWidth)
cap.set(4, frameHeight)
#cap.set(10, frameBrightness)

title = "Camera"

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow(title, img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break