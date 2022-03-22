def profile(name, age, main_lang):
    print("{0}\t{1}\t{2}".format(name, age, main_lang))

print("이름\t나이\t언어")
profile(name="둘리",main_lang="공룡어",age=100)
profile(age=33, name="고길동", main_lang="한국말")