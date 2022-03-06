# 나이순 정렬

import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().split()))
arr.sort(key=lambda x: int(x[0]))
for i in arr:
    print(i[0], i[1])