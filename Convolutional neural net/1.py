try:
	import cv2
	import numpy as np
	import scipy
	import dlib


except ImportError, err :
	print "couldn't load module. %s" % (err)
    sys.exit(2)

 def load_png(name):
    
    
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()

    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

 class con_detect():
  	def __init__(self, (xy), vector):
        
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('Ball.png')
        





 	def sum:
 		x1,y1=np.shape(image)
		temp=np.zeros((x1-x,y1-y))

		for i in range(0,x1-x):
			for j in range(0,y1-y):
				temp[i,j]=np.sum(image[i:i+x,j:j+y])/(x*y)
                        
		return temp

if __name__ == '__main__': main()
	