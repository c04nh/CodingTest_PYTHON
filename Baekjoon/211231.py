# 별 찍기 - 2

num = int(input())
for a in range(1, num + 1):
    for b in range(num - a, 0, -1):
        print(' ', end='')
    for c in range(1, a + 1):
        print('*', end='')
    print()