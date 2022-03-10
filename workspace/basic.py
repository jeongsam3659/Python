# 절대값

print(abs(-5)) #5
print(pow(4,2)) # 4^2 = 16
print(max(5, 12)) # 두 수 중 큰값 출력
print(min(5,12)) # 두 수 중 작은값

print(round(4.99)) # 반올림

from math import * # math 라이브러리를 *(모두) 이용하겠다는 말.
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근. = 4


# 랜덤 함수, 난수
from random import *
print(random()) # 0.0~ 1.0 미만의 임의값 생성.
print(random() * 10) # 0.0~ 10.0 미만의 임의값 생성.
print(int(random() * 10) +1) # 난수 정수화 # 1.0~ 10.0 이하의 임의값 생성.

print("로또번호 : "+str(int(random() * 45) +1))
#또는
print(randrange(1,46)) # 1~ 46미만의 임의의 갑 생성

print(randint(1,45)) # 1~ 45둘다 포함하는 임의 값 생성.