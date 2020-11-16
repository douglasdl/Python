import cv2

def getImage(picture = "my_pic.jpg"):
    # LOAD AN IMAGE USING 'IMREAD'
    img = cv2.imread(picture)
    # DISPLAY
    cv2.imshow("Picture",img)

def getVideo(video = "Resources/test_video.mp4"):
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(video)
    while True:
        success, img = cap.read()
        print(success)
        img = cv2.resize(img, (frameWidth, frameHeight))
        cv2.imshow("Result", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


#getImage()
getVideo(0)

cv2.waitKey(0)