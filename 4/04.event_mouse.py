# 마우스 이벤트 사용
import numpy as np
import cv2


def onMouse(event, x, y, flags, param):  # 콜백함수 - 이벤트 내용 출력
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_LBUTTONUP:
        print("마우스 왼쪽 버튼 떼기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 더블클릭")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("마우스 오른쪽 더블클릭")


image = np.full((200, 300), 255, np.uint8)  # 200행 300열 행렬을 흰색으로 초기화

title1, title2 = "Mouse Event1", "Mouse Event2"
cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback(title1, onMouse)  # 마우스 콜백함수 설정
cv2.waitKey(0)
cv2.destroyAllWindows()
