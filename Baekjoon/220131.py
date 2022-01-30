# ACM 호텔

T = int(input())
for i in range(T):
    arr = input().split()
    H = int(arr[0])
    W = int(arr[1])
    N = int(arr[2])
    if N % H == 0:
        print((H * 100) + (N // H))
    else:
        print(((N % H) * 100) + ((N // H) + 1))