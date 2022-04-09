# 최대공약수와 최소공배수

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
d = gcd(a, b)
print(d)
print(int(a * b / d))