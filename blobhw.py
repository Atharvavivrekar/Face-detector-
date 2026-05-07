import cv2
import numpy as np
image = cv2.imread("blob.png",1)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 50
params.filterByCircularity = True
params.minCircularity = 0.6
params.filterByConvexity = True
params.filterByInertia = True
params.minInertiaRatio = 0.03
params.minConvexity = 0.4
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(gray_image)
blank = np.zeros([1,1])
blobs = cv2.drawKeyPoints(image,keypoints,blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number = len(keypoints)
text = "Number of circles detected inside blobs" + str(number)
cv2.putText(blobs,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow("Filter circular blobs",blobs)
cv2.waitKey(0)

# Draw filled circle
cv2.circle(image, (x, y), r, (0, 255, 0), -1)

# Add text near each circle
cv2.putText(image, "Circle", (x - 20, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
            (255, 255, 255), 1, cv2.LINE_AA)