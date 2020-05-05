# USAGE
# python shape_detector.py --video *.mp4
# python shape_detector.py

# import the necessary packages

import cv2
import numpy as np
import imutils
from pg2 import ShapeDetector
from pg2 import ColorLabeler
from scipy.spatial import distance as dist
from collections import OrderedDict
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])

# keep looping
# if we are viewing a video and we did not grab a frame,
# then we have reached the end of the video
# grab the current frame
while True:
    (grabbed, img) = camera.read()
    if args.get("video") and not grabbed:
        break




    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)  # converting RGB to LAB format
    # blur = cv2.GaussianBlur(lab,(5,5),0)
    thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()
    cl = ColorLabeler()

    for c in cnts:
        M = cv2.moments(c)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except:
            print "failed to retrieve "
            cX=0
            cY=0

        shape = sd.detect(c)
        color = cl.label(lab, c)
        text = "{},{}".format(color, shape)
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)  # change location
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)  # location of the objects
        cv2.putText(img, text, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    cv2.imshow('blur', blur)
    cv2.imshow('thresh', thresh)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()