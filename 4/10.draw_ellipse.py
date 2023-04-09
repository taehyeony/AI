# 타원 및 호 그리기
import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)
image = np.full((300, 700, 3), 255, np.uint8)

pt1, pt2 = (180, 150), (550, 150)
size = (120, 60)

# 타원의 중심점 표시
cv2.circle(image, pt1, 1, 0, 2)  # (행렬,중심,반지름,색상,둘레 두께)
cv2.circle(image, pt2, 1, 0, 2)

# 타원 그리기
# (행렬,중심,(타원의 반지름 x축 길이,y축 길이),타원의 각도,호의 시작,호의 종료,색상,선의 두께)
cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)

# 호 그리기
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4)
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

cv2.imshow("Draw Ellipse", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
