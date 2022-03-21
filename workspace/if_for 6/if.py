weather = input("오늘 날씨는? : ")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("오늘은 맑습니다.")


print("----------------------------------")


temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 덥습니다. ")
elif 10 <= temp and temp <30:
    print("괜찮은 날씨. ")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 춥습니다.")