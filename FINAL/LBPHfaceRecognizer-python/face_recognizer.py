import cv2, os
import numpy as np
from PIL import Image
print "\n1.Imported all the Libraries"

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
print "\n2.Made the faceCascade Method"





def get_Faces_Labels_AndTrain(path , delay ):
    recognizer = cv2.createLBPHFaceRecognizer()
    print "\nMade the LBPH(LocalBinaryPatternHistogram) recognizer "
    print "Adding  PATH=",path
    image_paths = [os.path.join(path,f)  for f in os.listdir(path)if not f.endswith('.zzzzzzzzzzzzzz')]
    faces = []
    labels = []
    count = 0;
    for image_path in image_paths:
        print " getting the image"
        image_pil = Image.open(image_path).convert('L')
        print "Conv. to GrayScale "
        image_pil = np.array( image_pil ,  'uint8' )
        face = faceCascade.detectMultiScale( image_pil )
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", "")) 
        for (x, y, w, h) in face:

            count= count +1
            print "COUNT = " , count
            faces.append(image_pil [y: y + h, x: x + w])
            cv2.imshow("Adding faces to traning set...", image_pil[y: y + h, x: x + w])
            cv2.waitKey(delay)
            labels.append(nbr)
            print "recognizer updated... NUMBER OF FACES =", len(faces) , "Number of Lables =" , len(labels)
            recognizer.train(faces, np.array(labels))
            print "LABEL_NUMBER=", nbr
            if (count>3):
                nbr_predicted, conf = recognizer.predict( image_pil[y: y + h, x: x + w])
                print "PERCENT MATCH=",conf , "NUMBER PREDICTED = " , nbr_predicted
    cv2.destroyAllWindows()        
    print "USED THE GET FACES FUNCTION"
    return recognizer






print "\n4.Made the GetFaces&Labels Method"

def detect_face( path , delay , recognizer):
    print "PATH=",path
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
            count = count + 1
            print "COUNT = " , count
            nbr_predicted, conf = recognizer.predict( image_pil[y: y + h, x: x + w])
            print "PERCENT MATCH=",conf , "NUMBER PREDICTED = " , nbr_predicted
            cv2.imshow("ImageBeingChecked", image_pil[y: y + h, x: x + w])
            cv2.waitKey(delay)
    cv2.destroyAllWindows()        
    print "USED THE GET FACES FUNCTION"
    return 1
print "\n5.Made detect_face Method"


print "*****************************"

print "Recognizer build begin................................................................................................................................................................................................................................."
face_recognizer = get_Faces_Labels_AndTrain('./faces' , 1)
print "..................................................................................................................................................................................................................................Recognizer build Ends."
detect_face(path = './test', delay = 50 ,  recognizer = face_recognizer)










    

 



