import cv2

img = cv2.imread('osama.jpg' , -1)

print(img)

cv2.imshow('Windows Title Osama' , img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows
elif k == ord('s') :
    cv2.imwrite('Saved1.png' , img)
    print("Image Saved as Png")
    cv2.destroyAllWindows

