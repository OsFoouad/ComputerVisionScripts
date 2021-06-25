import  cv2
import numpy as np

def click_btn(event , x , y , flags , params) :
    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]
        nimg = np.zeros((512,512,3), dtype=np.uint8)
        nimg [ : ] = [b , g , r ] 
        cv2.imshow('new' , nimg)

img = cv2.imread('osama.jpg')


cv2.imshow('osama' , img)

cv2.setMouseCallback('osama' , click_btn)
cv2.waitKey(0)
cv2.destroyAllWindows