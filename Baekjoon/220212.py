# 네 번째 점

arr = [[0 for _ in range(2)] for _ in range(3)]
for i in range(3):
    arr[i][0], arr[i][1] = map(int, input().split())
x = arr[0][0]
y = arr[0][1]
for i in range(3):
    if arr[i][0] != x:
        x += arr[i][0]
        break
for i in range(3):
    if arr[i][1] != y:
        y += arr[i][1]
        break
x *= 2
y *= 2
x -= arr[0][0] + arr[1][0] + arr[2][0]
y -= arr[0][1] + arr[1][1] + arr[2][1]
print(x, y)