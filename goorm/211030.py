# 1단계
# 3과 5의 배수

user_input = input()
user_input = int(user_input)
sum = 0
for a in range(3, user_input + 1):
	if a % 3 == 0 or a % 5 == 0:
		sum += a
print(sum)