# 1단계
# 막대기

user_input = int(input())
stick = []
count = 1
for a in range(user_input):
	stick.append(int(input()))
long_stick = stick[user_input - 1]
for a in range(1, user_input):
	if stick[user_input - 1 - a] > long_stick:
		count += 1
		long_stick = stick[user_input - 1 - a]
print(count)
