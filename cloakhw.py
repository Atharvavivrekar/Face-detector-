import cv2, time
import numpy as np
cam_recorder = cv2.VideoCapture(1)

bg = 0
count = 0
time.sleep(2)

for i in range(60):
    ret,bg = cam_recorder.read()
    #print(ret,bg)

    if not ret:
        continue
bg = np.flip(bg,axis = 1)

while cam_recorder.isOpened():
    ret,frame = cam_recorder.read()
    if not ret:
        break
    frame = np.flip(frame, axis = 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35,50,50])
    upper_green = np.array([65,255,255])
    mask1 = cv2.inRange(hsv,lower_green,upper_green)
    lower_green = np.array([66,50,50])
    upper_green = np.array([85,255,255])
    mask2 = cv2.inRange(hsv,lower_green,upper_green)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations = 3)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 3)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(bg,bg,mask = mask1)
    res2 = cv2.bitwise_and(frame,frame,mask = mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("Invisibility cloak",final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break