# 1단계
# 3의 배수 게임

user_input = input()
for a in range(1, int(user_input) + 1):
	if a % 3 == 0:
		print('X', end=" ")
	else:
		print(f'{a}', end=" ")