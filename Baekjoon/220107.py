# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
cnt = [0 for a in range(10)]
for a in result:
    cnt[int(a)] += 1
for a in cnt:
    print(a)