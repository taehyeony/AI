# 원본 사진에 log값
import numpy as np
import cv2
import math


def mat_access1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i, j]  # 원소 접근 - mat1[i][j] 방식도 가능
            s = 100 * np.log(k + 1)
            image2[i, j] = s
            # image2.itemset(i,j,s)
            # img.itemset(i,j,0,math.log(1+k))


image = cv2.imread("images/log.jpg", cv2.IMREAD_GRAYSCALE)
image2 = np.array(image).reshape(293, 290)
img = np.array(image).reshape(293, 290)
# mat1 = np.arange(10).reshape(2, 5)
# mat2 = np.arange(10).reshape(2, 5)
# print(image2.shape)
# image_re = image2.reshape(-1)
mat_access1(image)
# image_re = image_re.reshape(293,290)
cv2.imshow("Image", image)
cv2.imshow("Image_", image2)
# cv2.imshow('Image2', image3)
cv2.waitKey()
