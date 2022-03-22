# def profile(name, age, food1, food2, food3, food4):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(food1, food2, food3, food4)

# profile("농심", 40, "신라면","안성탕면","짜파게티","너구리")

# 추가로 작성할 경우 함수를 수정해야하는데 
# 수정하지않은 방향으로 ' 가변 인수 '사용

def profile(name, age, *food):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in food:
        print(lang, end=" ")
    print()

profile("농심", 40, "신라면","안성탕면","짜파게티","너구리")
profile("오뚜기", 44, "진매","진순")