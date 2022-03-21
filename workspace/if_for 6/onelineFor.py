# 출석번호 1,2,3,4 앞에 100을 붙이기로 함 >>> 101,102, 103, 104....

students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students] 
# 100+i 값을 student에 넣는다.
# i는 students의 리스트값을 하나씩 불러와 실행
# 리스트로 넣는다.

print(students)
