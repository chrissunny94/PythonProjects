import numpy as np
import cv2
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
print "\n2.Made the faceCascade Object"
###################################

cap = cv2.VideoCapture(0)
count = 0
while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        cv2.imwrite("frame/frame.jpg" , gray )
        face = faceCascade.detectMultiScale( gray )
        for (x, y, w, h) in face:
                count= count +1
                print "COUNT = " , count
                IMG =gray[y: y + h, x: x + w]
                title = "frame/face.jpg"
                cv2.imwrite("frame/face" + str(count) +".jpg", IMG )
                cv2.imshow("Cropped Face", IMG)
                cv2.waitKey(20)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                  
                

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
