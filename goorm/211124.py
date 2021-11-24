# 1단계
# 의좋은 형제

import math

user_input = input()
arr = user_input.split(' ')
num = input()
jinwoo = int(arr[0])
sunwoo = int(arr[1])
temp = 0
for a in range(1, int(num) + 1):
	if a % 2 == 1:
		temp = math.ceil(jinwoo / 2)
		jinwoo -= temp
		sunwoo += temp
	else:
		temp = math.ceil(sunwoo / 2)
		sunwoo -= temp
		jinwoo += temp
print(jinwoo, sunwoo)