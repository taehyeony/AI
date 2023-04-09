# 마우스 이벤트 및 그리기 종합
import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)  # 파란색 사각형
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)  # 빨간색 원
            cv2.imshow(title, image)
            pt = (-1, -1)


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Event Draw"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)  # 마우스 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyAllWindows()
