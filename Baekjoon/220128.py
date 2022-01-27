# 달팽이는 올라가고 싶다

import math

arr = input().split()
A = int(arr[0])
B = int(arr[1])
V = int(arr[2])
cnt = math.ceil((V - B) / (A - B))
print(cnt)
