# 1단계
# 최소값

user_input = input()
user_input2 = input()
arr = user_input2.split(" ")
min = int(arr[0])
for a in range(1, len(arr)):
	if min > int(arr[a]):
		min = int(arr[a])
print (min)