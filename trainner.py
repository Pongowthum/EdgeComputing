import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHRecognizer()
path='dataSet'

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        prodImg=Image.open(imagePath).convert('L')
        prodNp=np.array(prodImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(prodNp)
        print (ID)
        IDs.append(ID)
        cv2.imshow("training",prodNp)
        cv2.waitKey(10)
    return IDs, faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
assure_path_exists('recognizer/')
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()