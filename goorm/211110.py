# 1단계
# 윤년 (Leap Year)

user_input = input()
year = int(user_input)
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print('Leap Year')
		else:
			print('Not Leap Year')
	else:
		print('Leap Year')
else:
	print('Not Leap Year')