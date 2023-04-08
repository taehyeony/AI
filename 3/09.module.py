# 모듈 임포트하기
import header_area as mod  # header_area 파일의 모듈로 임포트
from header_area import write  # header_area 파일 내 write함수만 임포트

mod.say()
area, msg = mod.calc_area(1, 5, 5)
write(area, msg)
