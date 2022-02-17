# 팩토리얼

def factorial(N):
    if N <= 1:
        return 1
    return N * factorial(N - 1)

N = int(input())
sum = factorial(N)
print(sum)
