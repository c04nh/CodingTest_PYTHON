# 나머지

arr = []
for a in range(10):
    arr.append(int(input()))
for a in range(10):
    arr[a] = arr[a] % 42
arr.sort()
cnt = 1
for a in range(1, 10):
    if arr[a] != arr[a - 1]:
        cnt += 1
print(cnt)