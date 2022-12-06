import cv2
import numpy as np
import warnings
import tensorflow as tf
import serial
warnings.filterwarnings("ignore")
from tensorflow.keras.models import load_model
model = load_model("vgg19model.h5")

arduino = serial.Serial('COM3',9800,timeout=1)
#arduino.open()
arduino.is_open
label = {0:"With Mask",1:"Without Mask"}
color_label = {0: (0,255,0),1 : (0,0,255)}
cap = cv2.VideoCapture("https://10.27.184.183:8080/video")
#address = "https://10.27.186.12:8080/video"
#cap.open(address)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while cap.isOpened():
    _,frame = cap.read()
    #frame = cv2.flip(frame, 1, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)#1.1,4
    for x,y,w,h in faces:
        resized_display = cv2.resize(frame, (600, 400))
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0))
        #roi_
        face_image = frame[y:y+h,x:x+w]
        resize_img  = cv2.resize(face_image,(128,128)) #128,128
        normalized = resize_img/255.0
        reshape = np.reshape(normalized,(1,128,128,3))#1,128,128,3
        reshape = np.vstack([reshape])
        result = model.predict(reshape)
        #result = np.round(model.predict(reshape))
        result = np.argmax(result, axis=1)[0]
        #result = np.argmax(result)


        cv2.rectangle(frame,(x,y),(x+w,y+h),color_label[result],3)
        cv2.rectangle(frame,(x,y-50),(x+w,y),color_label[result],-1)
        cv2.putText(frame,label[result],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

        if label[result] == "Without Mask":
            arduino.write(b'H')
            #print(label[result])
        else:
            arduino.write(b'L')
            #print(label[result])
        #elif result == 1:
            #cv2.rectangle(frame,(x,y),(x+w,y+h),color_label[1],3)
            #cv2.rectangle(frame,(x,y-50),(x+w,y),color_label[1],-1)
            #cv2.putText(frame,label[1],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)

    cv2.imshow("Checking",resized_display)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop
    if key == 27:  # The Esc key
        arduino.close()
        arduino.is_open
        break


cv2.destroyAllWindows()
cap.release()