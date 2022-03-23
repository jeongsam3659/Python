# 쓰기
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("국어 : 50", file=score_file)
score_file.close()

# 이어쓰기
score_file_up = open("score.txt", "a", encoding="utf-8")
print("과학 : 77", file=score_file_up)
print("\n코딩: 99", file=score_file_up)
score_file_up.close();

# 읽기
score_file_r = open("score.txt", "r", encoding="utf-8")
print(score_file_r.read())
score_file_r.close()

# 한줄씩 읽기
score_file_oner = open("score.txt", "r", encoding="utf-8")
print(score_file_oner.readline()) # 줄별로 읽기 / 한줄 읽고 커서는 다음줄로 이동
print(score_file_oner.readline())
score_file_oner.close()

