# 지역변수 / 전역변수

from tabnanny import check


gun = 10 #(1)

def checkpoint(soldier): 
    # gun = gun - soldier # gun >> (지역변수) # 초기화가 되어있지 않은 상태에선 사용할 수 없다.
    global gun # 전역공간에 있는 gun 사용(1)
    gun = gun - soldier
    print("[함수 내] 남은 수 : {0}".format(gun))

def checkpoint_ret(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 수 : {0}".format(gun))
    return gun

    # 함수의 전달값, 파라미터로 전달후 반환값으로 받는 방법.
    # 전역변수를 받아 지역변수로 처리후 반환값으로 하여
    # 전역변수의 결합도를 낮춘다.


print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun ,2)
print("남은 총 : {0}".format(gun))