# N과 M (4)

N, M = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, N + 1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)