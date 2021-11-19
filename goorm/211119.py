# 1단계
# Bubble Sort

user_input = int(input())
user_input2 = input()
arr = user_input2.split(' ')
nums = []
for a in arr:
	nums.append(int(a))
for a in range(0, user_input - 1):
	for b in range(0, user_input - a - 1):
		if nums[b] > nums[b + 1]:
			nums[b], nums[b + 1] = nums[b + 1], nums[b]
for a in nums:
	print(a, end=' ')