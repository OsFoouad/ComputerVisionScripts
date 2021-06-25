import cv2
import numpy as np

img = np.zeros([512  ,512 , 3] , np.uint8)
###### some possible shapes and also theres more
#Line
#img = cv2.line(img , (0 , 256) , (256 , 256) , (0 , 255,0) , 2 )
#arrowedLine
#img = cv2.arrowedLine(img , (0 , 256) , (256 , 256) , (0 , 255,0) , 2 )


#### closed shaped if thickness = -1 it will be filled

#rectanle
#img = cv2.rectangle(img , (50 , 50) , (460 , 460) , (255 , 0 ,0) ,2)
#circle
#img = cv2.circle(img , (256,256),100 ,(255,0,0) ,-1)
#text
#img = cv2.putText(img , 'Osama Fouad' , (10,256) , cv2.FONT_HERSHEY_SIMPLEX , 2, (255,0,0) , 4 )

cv2.imshow('Created Img' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

