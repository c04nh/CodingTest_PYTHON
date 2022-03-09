# N과 M (2)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]


def dfs(at, depth):
    if depth == M:
        for val in arr:
            print(val, end=' ')
        print()
        return
    for i in range(at, N + 1):
        arr[depth] = i
        dfs(i + 1, depth + 1)


dfs(1, 0)