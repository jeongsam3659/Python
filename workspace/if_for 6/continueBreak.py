absent = [2, 5] # 결석한 번호.
no_book = [7]

for student in range(1, 11):
    if student in absent:
        # 해당이 list에 포함되어있을시.
        continue
    elif student in no_book:
        print("{0}, 뒤에 가서 서있어.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))