# 벌집

N = int(input())
cnt = 1
range = 2
if N == 1:
    print(1)
else:
    while range <= N:
        range += 6 * cnt
        cnt += 1
    print(cnt)