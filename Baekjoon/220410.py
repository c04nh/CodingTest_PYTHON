# 최소공배수

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    d = gcd(a, b)
    print(a * b // d)
