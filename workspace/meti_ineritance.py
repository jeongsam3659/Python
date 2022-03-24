# 다중 상속.
# 2개이상의 상속을 받는것.
# ------------------------------------------
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    # 정의
    def __init__(self, name, hp, demage):
        Unit.__init__(self, name, hp)
        self.demage = demage

    # mathod1과 동일.
    # 공격시    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.demage))     
    
    # 뎀지계산
    def demaged(self, demage):
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name, demage))
        self.hp -= demage # 데미지 계산 # 현 체력 - 데미지
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1}방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 + 공격 + 유닛 클래스
class FlyableAtkUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, demage, flying_speed):
        AttackUnit.__init__(self, name, hp, demage)
        Flyable.__init__(self, flying_speed)


# 유닛 생성
valkyrie = FlyableAtkUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, valkyrie.flying_speed)

# 유닛2 생성
multal = FlyableAtkUnit("뮤탈", 150, 7, 4)
multal.fly(multal.name, "3시")