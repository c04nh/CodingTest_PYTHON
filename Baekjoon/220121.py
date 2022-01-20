# 상수

arr = input().split()
num1 = int(arr[0])
num2 = int(arr[1])
result1 = 0
result2 = 0
while num1 != 0:
    result1 = result1 * 10 + num1 % 10
    num1 //= 10
while num2 != 0:
    result2 = result2 * 10 + num2 % 10
    num2 //= 10
print(result1 if result1 > result2 else result2)