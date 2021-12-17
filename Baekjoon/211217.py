# 두 수 비교하기

user_input = input()
arr = user_input.split(' ')
num1 = int(arr[0])
num2 = int(arr[1])
if num1 > num2:
    print('>')
elif num1 < num2:
    print('<')
else:
    print('==')