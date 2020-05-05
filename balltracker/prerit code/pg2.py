import cv2
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		if len(approx) == 3:
			shape = "triangle"
		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
		elif len(approx) == 5:
			shape = "pentagon"
		else:
			shape = "circle"
		return shape



class ColorLabeler:
	def __init__(self):
		
		#colors = OrderedDict({"blue": (255, 0, 0),"green": (0, 255, 0),"red": (0, 0, 255),"new": (234,213,73)}) #this line is test, here new color was shown, but need fine tunning
		colors = OrderedDict({"blue": (255, 0, 0),"green": (0, 255, 0),"red": (0, 0, 255)})
		self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []
		for (i, (name, rgb)) in enumerate(colors.items()):
			self.lab[i] = rgb
			self.colorNames.append(name)
		self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

	def label(self, image, c):
		
		mask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		mask = cv2.erode(mask, None, iterations=2)
		mean = cv2.mean(image, mask=mask)[:3]
		minDist = (np.inf, None)
		for (i, row) in enumerate(self.lab):
			d = dist.euclidean(row[0], mean)
			if d < minDist[0]:
				minDist = (d, i)
		return self.colorNames[minDist[1]]