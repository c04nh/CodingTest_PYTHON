# 단어 정렬

import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().strip())
set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key = len)
for i in arr:
    print(i)