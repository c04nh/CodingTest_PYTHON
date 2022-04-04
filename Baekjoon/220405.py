# 잃어버린 괄호

subtraction = input().split('-')
arr = []
for i in subtraction:
    cnt = 0
    subtraction = i.split('+')
    for j in subtraction:
        cnt += int(j)
    arr.append(cnt)
N = arr[0]
for i in range(1, len(arr)):
    N -= arr[i]
print(N)