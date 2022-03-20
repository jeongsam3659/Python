# Life is too short를 출력하시오.

# 1
a = ['Life', 'is', 'too', 'short']

space =' '
result= a[0]+space+a[1]+space+a[2]+space+a[3]
print(result)

print("----------------------------------------------")

# 2
a = (1,2,3)
a = a+(4,)
print(a)

print("----------------------------------------------")

# 3
a = {'A':90, 'B':80, 'C':70}
# 'B'에 해당되는 값 추출.

result = a.pop('B')
print(a)
print(result)

print("----------------------------------------------")
# 4
# a 리스트에서 중복된 숫자들을 제거해보자
a = [1,1,1,2,2,3,3,3,4,4,5]

aSet = set(a)
print(aSet)
alist = list(aSet)
print(alist)
# SET형태는 중복을 갖지않는다.
