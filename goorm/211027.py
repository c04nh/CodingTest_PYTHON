# 1단계
# 소수 판별

user_input = input()
user_input = int(user_input)
for a in range(2, user_input):
	if user_input % a == 0:
		print("False")
		break
	if a == user_input - 1 and user_input % a != 0:
		print("True")