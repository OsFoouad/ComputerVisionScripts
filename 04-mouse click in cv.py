import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

def click_btn(event , x , y ,flags , param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ',' +  str(y)
        cv2.putText(img , strXY , (x,y) , font , .5 , (255,255,0) , 2  )
        cv2.imshow('osama' , img )

    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[x , y ,0]
        g= img[x,y,1]
        r= img[x,y,2]
        strBGR = str(b) + ',' + str(g) + ',' + str(r)
        cv2.putText(img , strBGR , (x,y) , font , .5 , (255,255,0) , 2  )
        cv2.imshow('osama' , img )



img  = cv2.imread('osama.jpg')
cv2.imshow('osama' , img)

cv2.setMouseCallback( 'osama' , click_btn)
cv2.waitKey(0)
cv2.destroyAllWindows
