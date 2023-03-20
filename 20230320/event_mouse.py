import numpy as np
import cv2

img = np.zeros((200,300,3),np.uint8)

def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼 누름')
        img[:] = (100,255,255)
        cv2.imshow(title1,img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('오른쪽 버튼 누름')
        img[:] = (255,100,255)
        cv2.imshow(title1,img)
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼 뗌')
    elif event == cv2.EVENT_RBUTTONUP:
        print('오른쪽 버튼 뗌')
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print('오른쪽 버튼 더블클릭')


title1, title2 = "Mouse Event1","Mouse Event2"
cv2.imshow(title1,img)
cv2.imshow(title2,img)

cv2.setMouseCallback(title1,onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()