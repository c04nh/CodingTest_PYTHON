# ATM

N = int(input())
arr = list(map(int, input().split()))
num = 0
arr.sort()
for i in range(N):
    for j in range(i + 1):
        num += arr[j]
print(num)