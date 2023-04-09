# 직선 & 사각형 그리기
import numpy as np
import cv2

# 색상 선언
# 파이썬은 (r,g,b)가 아닌 (b,g,r)로 저장하게 된다.
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)  # 400행 600열 3개 채널 생성
image[:] = (255, 255, 255)  # 3개 채널 흰색으로 초기화

# 좌표 선언
pt1, pt2 = (50, 50), (250, 150)
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100)  # 사각형 영역 (시작 x, 시작 y, width, height)

# 직선 그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, cv2.LINE_AA)

# 사각형 그리기
# (행렬, 시작 좌표, 종료 좌표, 색상, 두께, 옵션)
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
# 시작좌표가 (400,200)이고 크기가 100*100인 내부가 꽉찬 녹색 사각형
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED)

cv2.imshow("line & rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
