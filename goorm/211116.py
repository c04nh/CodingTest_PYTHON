# 1단계
# 비트 연산 기본 1

user_input = input()
arr = user_input.split(' ')
num1 = int(arr[0])
num2 = int(arr[1])
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)