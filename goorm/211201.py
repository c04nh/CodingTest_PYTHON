# 1단계
# 자동문

import math

user_input = input()
cnt = int(user_input)
length = []
a_arr = []
v = []
for a in range(cnt):
	user_input1 = input();
	arr = user_input1.split(' ')
	length.append(float(arr[0]))
	a_arr.append(float(arr[1]))
	v.append(float(arr[2]))
for a in range(cnt):
	time = math.sqrt(length[a] * 2 / a_arr[a])
	total = v[a] * time;
	print('{:.2f}'.format(total))