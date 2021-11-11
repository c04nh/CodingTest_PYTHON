# 1단계
# 몫과 나머지

user_input = input()
arr = user_input.split(' ')
a = int(arr[0])
b = int(arr[1])
print(f'{a // b} {a % b}')