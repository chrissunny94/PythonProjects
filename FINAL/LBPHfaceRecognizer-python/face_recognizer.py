import cv2, os
import numpy as np
from PIL import Image
print "\n1.Imported all the Libraries"

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
print "\n2.Made the faceCascade Method"


recognizer = cv2.createLBPHFaceRecognizer()
print "\n3.Made the LBPH(LocalBinaryPatternHistogram) Method "


def get_Faces_Labels_AndTrain(path = './faces'):
    
    print "PATH=",path
    
    
    print "LABELS=", np.array(labels)
    recognizer.train( faces ,np.array(labels  ))
    
    image_paths = [os.path.join(path,f)  for f in os.listdir(path)if not f.endswith('.zzzzzzzzzzzzzz')]
    faces = []
    labels = []
    count = 0;
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image_pil = np.array( image_pil ,  'uint8' )
        face = faceCascade.detectMultiScale( image_pil )
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", "")) 
        for (x, y, w, h) in face:
            count= count +1
            print "COUNT = " , count
            faces.append(image_pil [y: y + h, x: x + w])
            cv2.imshow("Adding faces to traning set...", image_pil[y: y + h, x: x + w])
            cv2.waitKey(50)
            labels.append(nbr)
            print "NUMBER =", nbr
            if (count>3):
                nbr_predicted, conf = recognizer.predict( image_pil[y: y + h, x: x + w])
                print "PERCENT MATCH=",conf , "NUMBER PREDICTED = " , nbr_predicted
            
    print "USED THE GET FACES FUNCTION"
    return faces, labels






print "\n4.Made the GetFaces&Labels Method"

def detect_face():
    path = './test'
    image_paths = os.listdir(path)
    print image_paths
    faces,labels = get_FACES_LABELS(path)
    cv2.destroyAllWindows()
    print "LABELS=", np.array(labels)
    print labels
    print faces
    faces = np.array(faces)
    faces = np.array( faces[0], 'uint8')
    nbr_predicted, conf = recognizer.predict(faces)
    print "PERCENT MATCH=",conf
    
print "\n5.Made detect_face Method"


print "*****************************"












    

 



