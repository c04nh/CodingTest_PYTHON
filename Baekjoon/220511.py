# 앵그리 창영

N, W, H = map(int, input().split())
for i in range(N):
    length = int(input())
    if W * W + H * H >= length * length: print("DA")
    else: print("NE")