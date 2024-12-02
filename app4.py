import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import streamlit as st
#step1
#---------------------import image and convert into rgb---------------
path="att_image"
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)
for cl in mylist:
    cuurnt_img=cv2.imread(f'{path}/{cl}')
    images.append(cuurnt_img)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)    
#---------------------encode the image ----------------------------
def encodings(images):
    encodelist=[]
    for img in images:
        cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode =face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
#------------------------Mark the attendence-----------------------------------
def markattendence(name):
    with open('attendence.csv','r+') as f:
        mydata=f.readline()
        namelist=[]
        #print(mylist)
        for line in mydata:
            entry=line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now =datetime.now()
            dtstring=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')    
       
#-----------------------use streamlit framework-----------------------------
encodelistknown=encodings(images)
print("encoding complete")
st.header("FACE ATTENDENCE USING BIO METRIC")
st.title("Welcome to attendence System")
st.video("veios/steptodown.com_665754.mp4")
st.image('att_image/biometric.png')
button= st.button("Take Attendnece")
# st.image('att_image/OIP.jpg')

if button:
    cap = cv2.VideoCapture(0)
    while True:
        success,img=cap.read()
        imgS=cv2.resize(img,(0,0),None,0.25,0.25)
        imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
        facecurrentframe=face_recognition.face_locations(imgS)
        encodecurrent =face_recognition.face_encodings(imgS,facecurrentframe)

        for encodeface,faceloc in zip(encodecurrent,facecurrentframe):
            matches=face_recognition.compare_faces(encodelistknown,encodeface)
            facedis=face_recognition.face_distance(encodelistknown,encodeface)
            #print(facedis)
            matchIndex=np.argmin(facedis)

            if matches[matchIndex]:
                name=classnames[matchIndex].upper()
                st.write("Your attendence is marked Thankyou",name)
                ballons=st.balloons()  
                print(name)
                y2,x2,y1,x1=faceloc
                y2,x2,y1,x1=y2*4,x2*4,y1*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,25),2)
                markattendence(name)
                        
        cv2.imshow("output",img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
          
        
    
        