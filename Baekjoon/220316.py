# 스타트와 링크

from itertools import combinations as c

N = int(input())
array = [i for i in range(N)]
matrix = []
for _ in range(N):
    matrix.append((list(map(int, input().split()))))
Min = int(1e9)
for r1 in c(array, N // 2):
    start, link = 0, 0
    r2 = list(set(array) - set(r1))
    for r in c(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in c(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    Min = min(Min, abs(start-link))
print(Min)