# 글자 쓰기
import numpy as np
import cv2

olive, violet, brown = (0, 128, 128), (221, 160, 221), (42, 42, 165)  # 색상 지정
pt1, pt2 = (50, 200), (50, 260)  # 좌표 지정

image = np.zeros((350, 500, 3), np.uint8)
image.fill(255)

# putText(행렬, 표시 문자열, 좌표, 폰트, 확대비율, 색상)
cv2.putText(image, "SIMPLEX", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, brown)
cv2.putText(image, "DUPLEX", (50, 130), cv2.FONT_HERSHEY_DUPLEX, 3, olive)
cv2.putText(image, "TRIPLEX", pt1, cv2.FONT_HERSHEY_TRIPLEX, 2, violet)
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC  # 글자체 상수
cv2.putText(image, "ITALIC", pt2, fontFace, 4, violet)

cv2.imshow("Put Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
