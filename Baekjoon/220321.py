# RGB거리

Red = 0
Green = 1
Blue = 2
N = int(input())
RGB = []
for i in range(N):
    RGB.append(list(map(int, input().split())))
for i in range(1, len(RGB)):
    RGB[i][Red] = min(RGB[i - 1][Green], RGB[i - 1][Blue]) + RGB[i][Red]
    RGB[i][Green] = min(RGB[i - 1][Red], RGB[i - 1][Blue]) + RGB[i][Green]
    RGB[i][Blue] = min(RGB[i - 1][Red], RGB[i - 1][Green]) + RGB[i][Blue]
print(min(RGB[N - 1][Red], RGB[N - 1][Green], RGB[N - 1][Blue]))