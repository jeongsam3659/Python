# 문자열 처리 함수

python_str = "Python is Amazing"
print(python_str.lower()) # 소문자
print(python_str.upper()) # 대문자
print(python_str[0].isupper()) #대상 문자가 대문자를 판별
print(len(python_str)) # 문자열 총 자리수
print(python_str.replace("Python", "Java"))
print(python_str.replace("python", "java")) # 대소문자 구별한다. 못할시 원본출력.

index = python_str.index("n") # 해당 문자 윗치값
print(index)
index = python_str.index("n", index +1) # 해당 문자 다음 자리값
print(index)

# 또는
print(python_str.find("java")) # .find일시에 원하는 값이 없을시 -1을 출력
# print(python_str.index("java")) # .index일시 오류 출력

print(python_str.count("n")) # 해당 문자 등장횟수