# 동전 0

N, K = map(int, input().split())
coin = [0] * N
for i in range(N):
    coin[i] = int(input())
cnt = 0
for i in range(N - 1, -1, -1):
    if coin[i] <= K:
        cnt += K // coin[i]
        K = K % coin[i]
print(cnt)
