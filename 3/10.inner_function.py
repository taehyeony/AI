# 내장함수 예제
a = [1.5, 2, 3, 4, 5]  # 리스트 생성
b = map(float, a)  # 실수 변환
c = divmod(5, 3)  # 몫과 나머지
print('최대값: ', max(a), '최솟값:', min(a))
print('몫과 나머지: ', c)
print('c의 자료형:', type(c), type(c[0]), type(c[1]))

print('2의 4제곱: ', pow(2, 4))
print('절댓값:', abs(-4))
