# 도형 넓이 구하기
# 도형 넓이 구하기
def calc_area(type, a, b, c=None):
    if type == 1:  # 사각형
        result = a * b
        msg = "사각형"
    elif type == 2:  # 삼각형
        result = a * b / 2
        msg = "삼각형"
    elif type == 3:  # 평행사변형
        result = (a + b) * c / 2
        msg = "평행사변형"
    return result, msg


def say():
    print("넓이를 구해요")


def write(result, msg):
    print(msg, '넓이는', result, 'm2입니다.')


say()
ret = calc_area(1, 5, 5)
area, msg = calc_area(2, 5, 5)
area2, _ = calc_area(3, 10, 7, 5)

print(type(ret))  # 튜플
print(type(area), type(msg))  # float,str
write(ret[0], ret[1])
write(area, msg)
write(area2, "평행사변형")
