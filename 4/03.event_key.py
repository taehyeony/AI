# 키 이벤트 사용
import numpy as np
import cv2

switch_case = {
    ord('a'): "a키 입력",  # ord() : 문자를 아스키코드로 변환
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",  # 0x42(16진수)를 10진수로 변환
    2424832: "왼쪽 화살표키 입력",  # 0x250000
    2490368: "윗쪽 화살표키 입력",  # 0x260000
    2555904: "오른쪽 화살표키 입력",  # 0x270000
    2621440: "아래쪽 화살표키 입력"  # 0x280000
}

image = np.ones((200, 300), np.float)  # 행렬을 실수형으로 표현(0~1)
cv2.imshow("keyboard Event", image)
while True:
    key = cv2.waitKeyEx(100)  # 키보드 입력 대기 100ms 동안 대기 시간동안 입력이 없으면 -1 리턴
    if key == 27:  # esc키를 누르면 종료
        break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
