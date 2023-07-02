import cv2
import numpy as np

def draw(mask,color):
    contornos,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000:
            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(frame, [c],0,color,3)

cap = cv2.VideoCapture(0)

blueLow = np.array([100,100,20], np.uint8)
blueHigh = np.array([125,255,255], np.uint8)

greenLow = np.array([50,100,20], np.uint8)
greenHigh = np.array([65,255,255], np.uint8)

redLow1 = np.array([0,100,20], np.uint8)
redHigh1 = np.array([5,255,255], np.uint8)

redLow2 = np.array([175,100,20], np.uint8)
redHigh2 = np.array([179,255,255], np.uint8)

while True:

    ret,frame = cap.read()

    if ret == True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV,blueLow,blueHigh)
        maskGreen = cv2.inRange(frameHSV,greenLow,greenHigh)
        maskRed1= cv2.inRange(frameHSV,redLow1, redHigh1)
        maskReed2 = cv2.inRange(frameHSV,redLow2,redHigh2)
        draw(maskBlue,(255,0,0))
        draw(maskGreen,(0,255,0))
        draw(maskRed1,(0,0,255))
        draw(maskReed2,(0,0,255))
        
        cv2.imshow('video',frame)


        if cv2.waitKey(1) & 0xFF ==ord('s'):
            break
cap.release()
cv2.destroyAllWindows()

