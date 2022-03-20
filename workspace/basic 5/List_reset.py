# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # set }

menu = list(menu)
print(menu, type(menu)) # list ]
# Set형을 List형으로 변경.

menu = tuple(menu)
print(menu, type(menu)) # tuple )

menu = set(menu)
print(menu, type(menu))