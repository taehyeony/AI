# 윈도우 이동
import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)  # 200행 400열 행렬 0으로 초기화
# 0~255 0:black 255:white
image[:] = 200  # 행렬을 밝은 회색으로 초기화

title1, title2 = 'Position1', 'Position2'  # 윈도우 이름설정
# 윈도우 생성 및 크기 조정 옵션
# 크기 조정 옵션 - 행렬의 크기에 맞게 자동 생성 - 크기 변경 불가
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)  # 윈도우 이동 - 위치 지정
cv2.moveWindow(title2, 400, 50)  # 가로 400px 세로 50px에 윈도우창 죄측 상단 꼭지점

cv2.imshow(title1, image)  # 행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.waitKey(0)  # 키 이벤트 대기
cv2.destroyAllWindows()  # 열린 모든 윈도우 파괴
