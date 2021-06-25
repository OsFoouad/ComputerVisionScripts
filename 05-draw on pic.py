import cv2
import numpy as np


def click_btn(event , x , y ,flags , param) :
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img , (x,y) , 15 , (0,0,255) , -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img , points[-1] , points[-2] , (255,0,0) , 4)
        cv2.imshow('osama' , img)





img  = cv2.imread('osama.jpg')
cv2.imshow('osama' , img)
points = []

cv2.setMouseCallback( 'osama' , click_btn)
cv2.waitKey(0)
cv2.destroyAllWindows
