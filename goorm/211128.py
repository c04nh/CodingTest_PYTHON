# 1단계
# 고장난 컴퓨터

user_input = input()
user_input2 = input()
arr1 = user_input.split(' ')
arr2 = user_input2.split(' ')
num1 = int(arr1[0])
num2 = int(arr1[1])
array = []
for a in arr2:
	array.append(int(a))
cnt = 1
for a in range(num1 - 1):
	if (array[a + 1] - array[a]) > num2:
		cnt = 1
	else:
		cnt += 1
print(cnt)