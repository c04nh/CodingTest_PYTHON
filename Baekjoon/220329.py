# 전깃줄

N = int(input())
wire = []
wire1 = []
dp = [0 for i in range(N)]
for i in range(N):
    wire.append(list(map(int, input().split())))
wire.sort(key = lambda x:x[0])
for i in range(N):
    wire1.append(wire[i][1])
for i in range(N):
    for j in range(i):
        if wire1[i] > wire1[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N - max(dp))