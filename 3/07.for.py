# 리스트 원소합 구하기
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0

for i in range(0, 5):  # 국어와 영어 점수의 총합
    sum1 = sum1 + kor[i] + eng[i]

for k in kor:  # 국어 점수의 총합
    sum2 = sum2 + k

for e in eng:  # 영어 점수의 총합
    sum2 = sum2 + e

for i, k in enumerate(kor):  # 리스트의 인덱스와 원소로 순회
    sum3 = sum3 + k + eng[i]

for k, e in zip(kor, eng):  # 여러 객체 동시 순회
    sum4 = sum4 + k + e

print("sum1=", sum1)
print("sum2=", sum2)
print("sum3=", sum3)
print("sum4=", sum4)
