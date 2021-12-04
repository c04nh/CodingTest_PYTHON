# 1단계
# 앵무새 꼬꼬

num = int(input())
input_arr = []
print_arr = []
for a in range(num):
	input_arr.append(input())
	string = ""
	for b in input_arr[a]:
		if b == 'A' or b == 'a' or b == 'E' or b == 'e' or b == 'I' or b == 'i' or b == 'O' or b == 'o' or b == 'U' or b == 'u':
			string += b
	if len(string) == 0:
		print_arr.append("???")
	else:
		print_arr.append(string)
	print(print_arr[a])

