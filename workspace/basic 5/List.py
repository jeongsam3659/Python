# 리스트 [] 
    # 순서를 가지는 객체의 집합.

from re import sub


subway = [10,20,30]

# 해당 수 서치.
ind_10 = subway.index(10)
print(ind_10) # 0

# 리스트 수 추가    .append(객체)
subway.append(50) 
print(subway)

# 사이에 넣기.      .insert(들어갈 번호, 객체)
subway.insert(1, 15)
print(subway)

# 빼기 (순서대로)   .pop()
print("빼기 : " +str(subway.pop()))
print(subway)

print("---------------------------------------------------------------")
#  ---------------------------------------------------------------

# 중복 유무         .count
people = ["유재석","박명수","정준하","정형돈","하하","노홍철","길"]
people.append("유재석")

print(people.count("유재석"))

# 정렬              .sort
num_list = [5,2,4,11,3]
num_list.sort()
print(num_list)

# 역정렬            .reverse
num_list.reverse()
print(num_list)

# 리스트 내용 삭제
num_list.clear()
print(num_list)


# 리스트는 자료형에 구애받지 않는다.
mix_list = ["사람", 22, True]
print(mix_list)

# 리스트 확장       .extend
subway1 = [10,20,30]
subway1.extend(mix_list)
print(subway1)