# N과 M (3)

N, M = map(int, input().split())
arr = []


def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr.append(i)
        dfs()
        arr.pop()


dfs()