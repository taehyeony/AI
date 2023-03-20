import numpy as np
import cv2

def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼 누름')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('오른쪽 버튼 누름')
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼 뗌')
    elif event == cv2.EVENT_RBUTTONUP:
        print('오른쪽 버튼 뗌')
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print('오른쪽 버튼 더블클릭')
img = np.full((200,300),255,np.uint8)

title1, title2 = "Mouse Event1","Mouse Event2"
cv2.imshow(title1,img)
cv2.imshow(title2,img)

cv2.setMouseCallback(title1,onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()