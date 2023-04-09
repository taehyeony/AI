# 마우스 및 트랙바 이벤트 사용
import numpy as np
import cv2


def onChange(value):  # 트랙바 콜백 함수
    global image, title  # 전역 변수 참조

    add_value = value - int(image[0][0])  # 트랙바 값과 영상 화소값 차
    print("추가 화소값:", add_value)
    image = image + add_value
    print(image)
    cv2.imshow(title, image)


def onMouse(event, x, y, flags, param):
    global image, bar_name

    # 마우스 우클릭시 밝기 10 증가
    if event == cv2.EVENT_RBUTTONDOWN:
        if image[0][0] < 246:
            image = image + 10
        else:
            image = np.full((300, 500), 255, np.uint8)
        # 트랙바 위치 변경 - 마우스로 클릭했을 때 트랙바의 위치 변경
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    # 마우스 좌클릭시 밝기 10 감소
    if event == cv2.EVENT_LBUTTONDOWN:
        if image[0][0] > 9:
            image = image - 10
        else:
            image = np.zeros((300, 500), np.uint8)
        # 트랙바 위치 변경 - 마우스로 클릭했을 때 트랙바의 위치 변경
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)
title = 'Trackbar & Mouse Event'
bar_name = 'Brightness'
cv2.imshow(title, image)
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
