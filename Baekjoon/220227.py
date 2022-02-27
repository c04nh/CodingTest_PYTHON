# 수 정렬하기

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
for i in arr:
    print(i)