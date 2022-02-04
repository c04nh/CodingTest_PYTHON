# 소수 찾기

import math

N = int(input())
numbers = map(int, input().split())
cnt = 0
for num in numbers:
    check = True
    if num == 1:
        continue
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            check = False
            break
    if check:
        cnt += 1
print(cnt)