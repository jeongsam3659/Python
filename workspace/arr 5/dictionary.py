# 사전
# Key 와 Value 구성으로 {key: value}로 정의된다.
human = {3: "유재석", 100:"김태호"}

print(human[3])
print(human[100])

# 또는

print(human.get(3))


# 주의사항.
# print(human[5]) # 없는 키를 사용시 에러가 발생한다고 바로 종료된다.

print(human.get(5)) # 반면 get을 사용시 ' None '으로 출력하고 넘어가는걸 볼 수 있다.
print(human.get(5, "해당 공간은 비어있습니다.")) # default 'None'대신 뒤에 문구로 출력할 수 있다.
print("None일시 넘어간다.")


# --------------------
# 해당 키가 있는 확인
print( 3 in human) # Boolean형태로 해당 Key가 있는 확인 여부를 묻는다.
print( 5 in human) # 없을시 false를 출력.


# --------------------
# Key값을 정수 대신 문자열로도 선언할 수 있다.
food = {"Ramen1": "신라면", "Ramen2": "안성탕면"}
print(food["Ramen1"])


# 사전 목록 추가
# 미리 해당 사전리스트를 사용중에는 그곳에 추가 된다.
food["Ramen3"] ="짜파게티"
print(food)

# 사전 목록 수정
food["Ramen1"] ="블랙 신라면"
print(food)

# 사전 목록 삭제
del food["Ramen2"]
print(food)

# 사전에 있는 Key값 확인
print(human.keys())

# 사전에 있는 value값 확인
print(human.values())

# 사전에 있는 Key,value값 둘다 확인
print(human.items())

# 사전 목록 초기화
food.clear()
print(food)