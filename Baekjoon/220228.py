# 수 정렬하기 2

import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    sys.stdout.write(str(i)+'\n')