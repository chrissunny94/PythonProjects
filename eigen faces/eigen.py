import numpy as NP
#For finding the EigenValues and EigenVectors
from scipy import linalg as LA



#Function to read the images

def read_images(path , sz=None):
	c=0
	X,y=[],[]    #Declaring the two variables for storing the List 
	for dirname , dirnames, filenames in os.walk(path):
		for subdirname in dirnames:
			subject_path = os.path.join( dirname , subdirname )
			for filename in os.listdir(subject_path):
				try:
					
					im = Image.open(os.path.join(subject_path, filename))
					im = im.convert("L")

					#if the default value of sz is not None then resize accordingly
					if (sz is not None):
						im = im.resize(sz, Image.ANTIALIAS)
					X.append(np.asarray( im , dtype= np .unit8))
					y.append(c)
				except IOError :
					print "I/O error:".format(errno,strerror)
				except :
					print "Unexpected error ".sys.exc_info()[0]
					raise
				c = c+1
	return [X,y]


read_images(./,)







