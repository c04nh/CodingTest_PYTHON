# 피보나치 수 5

def fibonacci(N):
    if N == 0: return 0
    if N == 1: return 1
    return fibonacci(N - 1) + fibonacci(N - 2)

N = int(input())
print(fibonacci(N))