# n번째에서 해당 루프 종료.

customer = "균민정"
index = 5
while index >= 1:
    print("{0}, 차례입니다. {1} 번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("{0}의 차례입니다. 들어오세요.".format(customer))


print("------------------------------------------")

person1 = "사람1"
count = 1
while(count < 11):
    print("{0} 회 진행하셨습니다. ( {1} )님".format(count, person1))
    count += 1


print("------------------------------------------")

person2 = "균민정"
unk_person = "Unknown"

while unk_person != person2:
    print("{0}, 제품이 준비되었습니다.".format(person2))
    unk_person = input("이름을 작성하세요: ")
