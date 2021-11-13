# 1단계
# 피라미드

user_input = input()
num = int(user_input)
for a in range(num):
	for b in range(num - 1 - a):
		print(' ', end='')
	for b in range(2 * a + 1):
		print('*', end='')
	print('')