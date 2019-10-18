import cv2
import numpy as np
import sqlite3

prodDetect=cv2.CascadeClassifier('haarcascade_object_default.xml')
rec=cv2.createLBPHRecognizer()
rec.load('recognizer/trainningData.yml')
id=0
camport=0

def getFromDB(Id):
    conn=sqlite3.connect("productdb.db")
    cmd="SELECT * FROM product WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    record=None
    for row in cursor:
        record=row
    conn.commit()
    conn.close()
    return record

def productMatched(Id,Name):
    print (Id)
    conn=sqlite3.connect("Product.db")
    cmd="SELECT * FROM detectedProducts WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE detectedProducts SET name='"+str(Name)+"' WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO detectedProducts(ID,name) VALUES('"+str(Id)+"','"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

cam=cv2.VideoCapture(camport)
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,4)

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=prodDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getFromDB(id)
        if(conf<50):
            if(profile!=None):
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                #cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[0]),(x,y+h),font,255)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,255)
                productMatched(profile[0],str(profile[1]))
        else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("WEB CAM OBJECT DETECTION",img)
    if(cv2.waitKey(1)==ord('q')):
       break
cam.release()
cv2.destroyAllWindows()