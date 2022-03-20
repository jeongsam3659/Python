# 집합 ( Set )
# 중복 x , 순서 x

mySet = {1,2,3,3,4}
print(mySet)

# --------------------------------
MBC = {"유재석","박명수","정준하"}
SBS = set(["유재석","지석진"])

# 교집합
print(MBC & SBS)
print(MBC.intersection(SBS))

# 합집합
print(MBC | SBS)
print(MBC.union(SBS))

# 차집합
print(MBC - SBS)
print(MBC.difference(SBS))

# 집합에 추가
SBS.add("하하")
print(SBS)

# 집합에 제거
SBS.remove("지석진")
print(SBS)