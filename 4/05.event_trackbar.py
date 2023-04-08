# 트랙바 이벤트 사용
import numpy as np
import cv2


def onChange(value):  # 트랙바 콜백 함수
    global image, title  # 전역 변수 참조

    add_value = value - int(image[0][0])  # 트랙바 값과 영상 화소값 차
    print("추가 화소값:", add_value)
    image = image + add_value
    print(image)
    cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

# 트랙바 콜백 함수
cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)
#                   트랙바 이름, 윈도우 이름, 현재값, 최대값, 콜백함수
cv2.waitKey(0)
cv2.destroyAllWindows()
