import pickle

# 파일 일기
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt","r", encoding="utf8" ) as study_file:
    print(study_file.read())