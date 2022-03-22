# 표준 입출력.

print("python","Java","C++", sep=" A ")
print("python","Java","C++", end="? ")

import sys
print("1python","1JAVA", file=sys.stdout)

print("-------------------------------------------------------------")

# 정렬
# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ")


print("-------------------------------------------------------------")

# 은행 대기순번표
# 001, 002, 003, ....
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

print("-------------------------------------------------------------")

answer = input("아무거나 입력하세요 : ")
print("입력값 : "+ answer)
