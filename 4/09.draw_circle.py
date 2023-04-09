# 원 그리기
import numpy as np
import cv2

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)
image = np.full((300, 500, 3), 255, np.uint8)

print(image.shape)
center = (image.shape[1] // 2, image.shape[0] // 2)  # 화면 중심 좌표
pt1, pt2 = (300, 50), (100, 200)
shade = (pt2[0] + 2, pt2[1] + 2)  # 그림자 좌표

# 원 그리기
# circle(행렬, 중심 좌표, 반지름, 색상, 둘레 두께)
cv2.circle(image, center, 100, blue)
cv2.circle(image, pt1, 50, orange, 2)
cv2.circle(image, pt2, 70, cyan, -1)  # 두께에 -1을 넣으면 내부가 fill된다.

# 글씨와 그림자효과
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "pt1_orange", pt1, font, 0.8, orange)
cv2.putText(image, "center_blue", center, font, 1, blue)
# 마지막 인자는 글씨의 두께를 의미한다.
cv2.putText(image, "pt2_cyan", shade, font, 0.8, black, 2)
cv2.putText(image, "pt2_cyan", pt2, font, 0.8, cyan, 1)

cv2.imshow("Draw Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
