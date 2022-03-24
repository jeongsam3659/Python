# 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("[{0}]: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격유닛 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("[{0}]: {1} 방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def demaged(self, damage):
        print("[{0}]: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("[{0}]: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("[{0}] 가 파괴었습니다.".format(self.name))

# 공중
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("[{0}]: {1}방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 + 공격 + 유닛 클래스
class FlyableAtkUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, demage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, demage) # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    # move() 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location