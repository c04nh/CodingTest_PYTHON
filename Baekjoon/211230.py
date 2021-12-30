# 별 찍기 - 1

num = int(input())
for a in range(1, num + 1):
    for b in range(1, a + 1):
        print('*', end='')
    print()