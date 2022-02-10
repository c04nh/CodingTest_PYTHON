# 직사각형에서 탈출

arr = input().split()
x = int(arr[0])
y = int(arr[1])
w = int(arr[2])
h = int(arr[3])
x_min = min(x, w - x)
y_min = min(y, h - y)
print(min(x_min, y_min))