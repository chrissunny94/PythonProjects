import numpy as np
import cv2
import time
cascadePath = "cascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
print "\n2.Made the faceCascade Object"
###################################

def get_WebCamFeed(timer , delay , Cascade):
        cap = cv2.VideoCapture(0)
        count = 0
        while(True):
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame',gray)
                cv2.imwrite("frame/frame.jpg" , gray )
                face = Cascade.detectMultiScale( gray )
                for (x, y, w, h) in face:
                        count= count +1
                        print "COUNT = " , count
                        IMG =gray[y: y + h, x: x + w]
                        cv2.imwrite("frame/face" + str(count) +".jpg", IMG )
                        cv2.imshow("Cropped Face", IMG)
                        cv2.waitKey(10)
                time.sleep(delay)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
        print "USED THE get_WebCamFeed function"         
        cap.release()
        cv2.destroyAllWindows()



get_WebCamFeed(timer = 10 ,delay = .1 ,Cascade = faceCascade )
