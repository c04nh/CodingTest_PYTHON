# 소수

M = int(input())
N = int(input())
sum = 0
min = N
for i in range(M, N + 1):
    result = 0
    if i == 1:
        result += 1
        continue
    for j in range(2, i):
        if i % j == 0:
            result += 1
            break
    if result == 0:
        sum += i
        if min > i:
            min = i
if sum == 0: print(-1)
else:
    print(sum)
    print(min)