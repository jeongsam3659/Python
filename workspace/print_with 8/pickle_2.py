import pickle
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기

print(profile)
profile_file.close()


