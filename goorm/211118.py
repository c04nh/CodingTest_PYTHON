# 1단계
# 세로 순서 사각형

user_input = input()
num = int(user_input)
for a in range(1, num + 1):
	for b in range(a, a + num * (num - 1) + 1, num):
		print(b, end=" ")
	print()