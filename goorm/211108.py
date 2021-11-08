# 1단계
# 모양찍기

user_input = input()
num = int(user_input)
for a in range(1, num + 1):
	for b in range(num + 1 - a):
		print('*', end="")
	print()