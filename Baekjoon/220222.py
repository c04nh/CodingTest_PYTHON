# 블랙잭

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
             temp = arr[i] + arr[j] + arr[k]
             if arr[i] + arr[j] + arr[k] <= M:
                 result = max(result, arr[i] + arr[j] + arr[k])
print(result)