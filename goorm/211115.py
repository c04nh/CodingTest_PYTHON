# 1단계
# Substring

user_input = input()
user_input2 = input()
arr = user_input2.split(" ")
num1 = int(arr[0])
num2 = int(arr[1])
print(user_input[num1 - 1 : num1 + num2 - 1])