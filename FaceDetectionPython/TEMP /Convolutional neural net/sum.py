import cv2
import numpy as np


#This is the sum CNN funtion , for convolution
#sum_cnn(image,window size x, window size y)
def sum_cnn(image,x,y):
	

	x1,y1=np.shape(image)
	temp=np.zeros((x1-x,y1-y))

	for i in range(0,x1-x):
		for j in range(0,y1-y):
			temp[i,j]=np.sum(image[i:i+x,j:j+y])/(x*y)
                        
	return temp
	
	
	







image =cv2.imread('test.jpg')
#image=cv2.grayscale(image)

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=np.matrix(image)
image=cv2.resize(image,(93,93))



print image

x1,y1=np.shape(image)


temp=sum_cnn(image,10,10)
print (np.sum(image))
print x1
print y1
print temp

cv2.imwrite('1.jpg',temp)
print np.sum(temp)