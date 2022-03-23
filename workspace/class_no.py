# 클래스화

m_name = "마린"
m_hp = 40  # 체력
m_demage = 5 # 유닛의 공격력


print("{0} .유닛이 생성되었습니다.".format(m_name))
print("체력:{0}\n공격력:{1}\n".format(m_hp,m_demage))

z_name = "저글링"
z_hp = 20
z_demage = 7

print("{0} 유닛이 생성되었습니다.".format(z_name))
print("체력:{0}\n공격력:{1}\n".format(z_hp,z_demage))

def attack(name, location, demage):
    print("{0} : {1} 방향으로 적군을 공격. [공격력 {2}]".format(name, location, demage))



attack(m_name, "1시", m_demage)
attack(z_name, "3시", z_demage)

#  이렇게 하면 한번 호출할때마다 새 변수화를 계속늘려야한다.