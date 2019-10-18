import cv2
import sqlite3
import numpy as np

prodDetect=cv2.CascadeClassifier('haarcascade_object_default.xml')
cam=cv2.VideoCapture(0)

def insertOrUpdate(Id,Name,price,weight):
    conn=sqlite3.connect("productdb.db")
    cmd="(SELECT * FROM product WHERE ID='"+str(Id)+")'"
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE product SET name='"+str(Name)+"' ,price='"+str(price)+"' ,weight='"+str(weight)+"' WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO product(ID,name,price,weight) VALUES('"+str(Id)+"','"+str(Name)+"','"+str(price)+"','"+str(weight)+"')"
        
    conn.execute(cmd)
    conn.commit()
    conn.close()
   
id=int(input('ENTER ID'))
name=input('ENTER NAME')
price=int(input('ENTER PRICE'))
weight=int(input('ENTER Weight'))
insertOrUpdate(id,name,price,weight)
sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    products=prodDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in products:
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/product."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(10)
    cv2.imshow("WEB CAM OBJECT DETECTION",img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
cam.release()
cv2.destroyAllWindows()