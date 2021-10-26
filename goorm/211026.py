# 1단계
# 특정 구간의 합

user_input = input()
arr = input()
arr = arr.split(" ")
tmp = input()
tmp = tmp.split(" ")
sum_num = 0
for a in range(int(tmp[0]) - 1, int(tmp[1])):
	sum_num += int(arr[a])
print(sum_num)