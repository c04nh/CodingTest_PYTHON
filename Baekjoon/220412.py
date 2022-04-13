# 링

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

N = int(input())
arr = list(map(int, input().split()))
firstRing = arr[0]
for i in range(1, N):
    otherRing = arr[i]
    gcdNum = gcd(firstRing, otherRing)
    print(f'{firstRing // gcdNum}/{otherRing // gcdNum}')
