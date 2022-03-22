def profile(name, age, main_lang):
    print("이름 : {0}\t나이: {1}\t 과목: {2}"\
        .format(name, age, main_lang))

profile("균민정", 27, "JS")
profile("구구구", 99, "구구콘")

# \을 사용하면 코드상 이어져있고 한칸enter하여 쓸수있다.


print("------------------------------------------------------")

def school_pro(name1, age1=17, main_lang1="JS"):
    print("이름 : {0}\t나이: {1}\t 과목: {2}"\
    .format(name1, age1, main_lang1))

school_pro("둘리")
school_pro("또치")