# 1단계
# 단어의 개수 세기

user_input = input()
arr = user_input.split(' ')
count = 0
for a in arr:
	if a != '':
		count += 1
print(count)