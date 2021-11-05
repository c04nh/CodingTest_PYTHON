# 1단계
# Min 함수

user_input = input()
arr = user_input.split(" ")
min_num = min(int(arr[0]), int(arr[1]))
print(min_num)

def min(a, b):
	if a > b:
		min = a
	else:
		min = b
	return min