import cv2 as cv

img = cv.imread('mybaby.jpg')
img1 = cv.line(img,(0,0),(511,511),(255,0,0),5)
img2 = cv.rectangle(img1,(384,0),(510,128),(0,255,0),3)
img3 = cv.circle(img2,(400,130),63,(0,0,255),-1)
img4 = cv.ellipse(img3,(256,256),(100,50),0,0,180,255,-1)

cv.imshow('image',img2)
cv.waitKey(0)
cv.destroyAllWindows()
