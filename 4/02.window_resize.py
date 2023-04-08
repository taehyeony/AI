# 윈도우의 크기 변경
import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)  # ndarray생성 - 200행 300열 8비트 정수형
image.fill(255)  # image를 흰색으로 채움

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # 윈도우 생성 - 크기변경 불가
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)  # 윈도우 생성 - 크기 변경 가능

cv2.imshow(title1, image)  # 행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)  # 윈도우 크기 변경 - 400행 300열
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()
