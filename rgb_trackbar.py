import numpy as np
import cv2
def onChange(pos):
    global image
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    image[:] = (b,g,r)
    cv2.imshow('image',image)
    
image = np.zeros((300,500,3),np.uint8)
cv2.imshow('image',image)

cv2.createTrackbar("R", 'image', 128, 255, onChange)
cv2.createTrackbar("G", 'image', 128, 255, onChange)
cv2.createTrackbar("B", 'image', 100, 255, onChange)
cv2.waitKey(0)													# 키 입력 대기
cv2.destroyAllWindows()                                	# 모든 윈도우 닫기