# 손익분기점

arr = input().split()
A = int(arr[0])
B = int(arr[1])
C = int(arr[2])
if C <= B:
    print(-1)
else:
    print(int(A / (C - B)) + 1)