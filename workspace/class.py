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


# ex) Unit >> 클래스 / marine1, marine2 >> 인스턴스