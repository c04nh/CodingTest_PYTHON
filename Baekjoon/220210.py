# 골드바흐의 추측

prime = [False, False] + [True] * 10000

for i in range(2, 101):
    if prime[i] == True:
        for j in range(i + i, 10001, i):
            prime[j] = False

T = int(input())
for i in range(T):
    N = int(input())
    num = N // 2
    for j in range(num, 1, -1):
        if prime[N - j] and prime[j]:
            print(j, N - j)
            break