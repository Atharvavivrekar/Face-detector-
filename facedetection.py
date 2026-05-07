import cv2
import os

video = cv2.VideoCapture(1)
#face_cascade = cv2.CascadeClassifier("facedetection.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

count = 0 
while video.isOpened():
    ret,frame = video.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,5)
    print(len(faces))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Face detected",frame)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()