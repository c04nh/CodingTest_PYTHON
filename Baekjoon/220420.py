import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]
temp = 0
for i in arr:
    temp += i
    dp.append(temp)
for i in range(M):
    a, b = map(int, input().split())
    print(dp[b] - dp[a - 1])
