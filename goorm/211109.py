# 1단계
# 공백 없애기

user_input = input()
for a in user_input:
	if a != " ":
		print(a, end = "")