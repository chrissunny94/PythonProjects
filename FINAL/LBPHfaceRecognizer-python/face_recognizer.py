import cv2, os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

print "\n1.Imported all the Libraries"
##################################

cascadePath = "cascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
print "\n2.Made the faceCascade Object"
###################################

def get_Faces_Labels_AndTrain_LBPH(path , delay ):
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
            IMG =image_pil[y: y + h, x: x + w]
            cv2.imshow("Adding faces to traning set...", image_pil[y: y + h, x: x + w])
            #plt.imshow(IMG, cmap = 'gray', interpolation = 'bicubic')
            #plt.xticks([]), plt.yticks([])
            #plt.show()
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
    print "Returing the Recognizer"
    return recognizer
print "\n4.Made the get_Faces_Labels_AndTrain_LBPH(path , delay ), returns recognizer Method"







###################################################################################
def detect_face_LBPH( path , delay , recognizer):
    print "PATH=",path
    image_paths = [os.path.join(path,f)  for f in os.listdir(path)if not f.endswith('.jpg')]
    faces = []
    labels = []
    for image_path in image_paths:
        print "ImageName =" , image_path
        image_pil = Image.open(image_path).convert('L')
        image_pil = np.array( image_pil ,  'uint8' )
        faces = faceCascade.detectMultiScale( image_pil )
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        print " # TESTFILE =",nbr
        count = 1;
        click = 0;
        for (x, y, w, h) in faces:
            count = 1
            click = 0
            count = count + 1
            nbr_predicted, conf = recognizer.predict( image_pil[y: y + h, x: x + w])
            print "Coef=",conf , "NUMBER PREDICTED = " , nbr_predicted
            if (nbr == nbr_predicted):
                print "Match...................."
                click=click +1
                cv2.imshow("ImageBeingChecked", image_pil[y: y + h, x: x + w])
                cv2.waitKey(delay)

        print count , click    
    print "PERCENT MATCH=",((100*click)/count)
    cv2.destroyAllWindows()        
    print "USED THE GET FACES FUNCTION"
    return 1
print "\n5.Made detect_face_LBPH( path , delay , recognizer) Method"
###########################################################

def get_registry_entry(roll_number, register_filename):
    """
    Returns: str name, int frequency from register_filename. It requires roll_number integer.
    """
    with open(register_filename, "r") as f:
        register = f.read()

    register_list = register.split("\n")[1:] #list slicing removes header
    register_list_list = [e.split(",") for e in register_list]
    register_entry_dict = {int(e[0]):(e[1],e[2]) for e in register_list_list}

    name, frequency = register_entry_dict[roll_number]

    return name, int(frequency)

def update_registry_entry(roll_number, name, frequency, register_filename):
    """
    Updates entry corresponding to the roll_number in register_filename
    """
    with open(register_filename, "r") as f:
        register = f.read()

    register_header = register.split("\n")[:1]
    register_list = register.split("\n")[1:]
    register_list_list = [e.split(",") for e in register_list]
    register_entry_dict = {e[0]:(e[1],e[2]) for e in register_list_list}

    #update register_entry_dict
    register_entry_dict[str(roll_number)] = (name, str(frequency))
    register_list_updated = [",".join([x, register_entry_dict[x][0], register_entry_dict[x][1]]) for x in register_entry_dict]
    register_updated = "\n".join(register_header+register_list_updated)
    
    with open(register_filename, "w") as f:
        f.write(register_updated)
#############################################################################################################











print "**************************************************INIT**********************************************************************"
#update_registry_entry()














print "***************************** MAIN TEST PROGRAM STARTS HERE*****************************************************************************************************"

print "Recognizer build begin................................................................................................................................................................................................................................."
face_recognizer = get_Faces_Labels_AndTrain_LBPH('./faces' , 1)
print "..................................................................................................................................................................................................................................Recognizer build Ends."
detect_face_LBPH(path = './test', delay = 1 ,  recognizer = face_recognizer)













    

 



