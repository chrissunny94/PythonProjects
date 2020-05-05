import cv2
import numpy as np
import imutils
from pg2 import ShapeDetector 
from pg2 import ColorLabeler
from scipy.spatial import distance as dist
from collections import OrderedDict

img = cv2.imread('sample.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) 
blur = cv2.GaussianBlur(gray,(5,5),0)
lab = cv2.cvtColor(img,cv2.COLOR_RGB2LAB) #converting RGB to LAB format
#blur = cv2.GaussianBlur(lab,(5,5),0)
thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()
cl = ColorLabeler()

for c in cnts:
	M = cv2.moments(c)
	cX = int(M["m10"]/M["m00"])
	cY = int(M["m01"]/M["m00"])
	shape = sd.detect(c)
	color = cl.label(lab,c)
	text = "{},{}".format(color,shape)
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2) # change location 
	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1) #location of the objects
	cv2.putText(img, text, (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()