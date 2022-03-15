'''
    사이트별로 비밀번호를 만들어 주는 프로그램을 작성.
    EX) http://naver.com

    규칙1 : http://  부분은 제외 >> naver.com
    규칙2 : 처음 만나는 점(.) 이후 부분은 제외 >> naver
    규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e'갯수 + "!" 로 구성.
'''

url = "http://naver.com"

# 규칙1
str1_url = url.replace("http://", "")


# 규칙2
str2_url = str1_url[:str1_url.index(".")]
# 슬라이싱을 활용하여 자른다 .>> 범위 지정시 .index()로 "."까지 수를 구한후 적용.


# 규칙3
str3_url = str2_url[:3]
cnt_url = str(len(str2_url))
e_url = str(str2_url.count("e"))

pwd_url = str3_url+cnt_url+e_url+"!"
print("{0} 의 사이트 비밀번호는: {1} 입니다.".format(url, pwd_url))