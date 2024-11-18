import cv2 
import pickle
import numpy
import datetime
import streamlit as st

def processing(img):
    a=0
    for pos in slots:
        
        imgCrop = img[pos[0][1]:pos[1][1], pos[0][0]:pos[1][0]]
        count = cv2.countNonZero(imgCrop)

        if count<250:
            color = (0,255,0)
            a +=1
            thickness = 5
        else:
            color = (0,0,255)
            thickness = 2
        cv2.rectangle(frame,pos[0],pos[1],color,thickness)
    cv2.putText(frame,str(datetime.datetime.now()) , (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)
    text = str(a) + "/" +str(len(slots))
    cv2.putText(frame, text, (10,75), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 5)

       
try:
    with open("file","rb") as f:
       slots = pickle.load(f)
except:
    slots =[]

cam = cv2.VideoCapture(0) #for system camera
# cam = cv2.VideoCapture(1) #for external camera 
# cam = cv2.VideoCapture("https://192.168.0.100:8080/video") #camera on ip ---> change ip accordingly and also add '/video' to ip

st.title(':[PARKING VIDEO]')
frame_placeholder = st.empty()
stop_button_pressed = st.button("Stop")

a = []


while cam.isOpened:
    ret, frame = cam.read()
    frame = cv2.resize(frame,(1000,600))

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img = cv2.medianBlur(img, 3)
    kernal = numpy.ones((1,1), numpy.uint8)
    img = cv2.dilate(img, kernal)
    processing(img)
                
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB")

   
    if cv2.waitKey(1) == ord('/') or stop_button_pressed:
        break  


cam.release()
cv2.destroyAllWindows()