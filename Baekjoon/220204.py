# Fly me to the Alpha Centauri

import math

T = int(input())
for i in range(T):
    arr = input().split()
    X = int(arr[0])
    Y = int(arr[1])
    distance = Y - X
    max = int(math.sqrt(distance))
    if max == math.sqrt(distance):
        print(max * 2 - 1)
    elif distance <= max * max + max:
        print(max * 2)
    else:
        print(max * 2 + 1)