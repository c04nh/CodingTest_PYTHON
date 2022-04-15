# 패션왕 신해빈

from collections import Counter

T = int(input())
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        a, b = input().split()
        arr.append(b)
    num = 1
    result = Counter(arr)
    for i in result:
        num *= result[i] + 1
    print(num - 1)
