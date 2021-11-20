# 1단계
# 거스름돈

user_input = input()
price = 1000 - int(user_input)
coin = [0, 0, 0, 0]
while price > 0:
	if price >= 500:
		price -= 500
		coin[0] += 1
	elif price >= 100:
		price -= 100
		coin[1] += 1
	elif price >= 50:
		price -= 50
		coin[2] += 1
	else:
		price -= 10
		coin[3] += 1
for a in coin:
	print(a, end=' ')