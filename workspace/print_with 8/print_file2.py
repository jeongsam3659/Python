
#파일을 한줄씩 읽다가 없을경우 반복문 종료 후 출력.
score_file = open("score.txt","r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)

score_file.close()