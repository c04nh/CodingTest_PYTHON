# 소트인사이드

N = int(input())
arr = list(map(int, str(N)))
arr.sort(reverse=True)
for i in arr:
    print(i, end='')