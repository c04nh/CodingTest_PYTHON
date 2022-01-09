# 평균

num = int(input())
user_input = input()
arr = user_input.split(' ')
for a in range(len(arr)):
    arr[a] = int(arr[a])
max_num = max(arr)
for a in range(len(arr)):
    arr[a] = arr[a] / max_num * 100
total = sum(arr)
print(total / len(arr))