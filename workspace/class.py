# ex) Unit >> 클래스 / marine1, marine2 >> 인스턴스
class Unit:
    def __init__(self, name, hp, demage):
        self.name = name
        self.hp = hp
        self.demage = demage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.demage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.demage))

wraith2 = Unit("레이스2", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# wraith1 과 wraith2의 차이점은 2애는 멤버변수(.clocking)을 true로 설정해 사용할 수 있다.
# 1은 사용할 수 없다.