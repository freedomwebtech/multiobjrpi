import cv2
import numpy as np
cap=cv2.VideoCapture(0)

lower_range=np.array([152,130,150])
upper_range=np.array([179,166,255])
blower_range=np.array([98,168,130])
bupper_range=np.array([179,255,255])
ylower_range=np.array([11,85,150])
yupper_range=np.array([73,165,232])


def redcolor(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range,upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("red"),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
def bluecolor(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,blower_range,bupper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("blue"),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
def yellowcolor(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,ylower_range,yupper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("yellow"),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)            

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    redcolor(frame)
    bluecolor(frame)
    yellowcolor(frame)
    
            
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(32)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
