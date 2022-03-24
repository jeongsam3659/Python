# 상속.
# -----------------------------------------------------------
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

# 유닛1
firebat1 = AttackUnit("파이어뱃",50 ,16) # name / hp / demage
firebat1.attack("5시")

firebat1.demaged(25)
firebat1.demaged(25)