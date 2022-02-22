# 분해합

N = int(input())
result = 0
for i in range(N):
    number = i
    sum = 0
    while(number != 0):
        sum += number % 10
        number //= 10
    if sum + i == N:
        result = i
        break
print(result)