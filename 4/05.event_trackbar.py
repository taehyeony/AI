# 트랙바 이벤트 사용
import numpy as np
import cv2


def onChange(value):  # 트랙바 콜백 함수
    global image, title  # 전역 변수 참조
