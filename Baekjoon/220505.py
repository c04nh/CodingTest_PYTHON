# 나머지 합

import sys
input = sys.stdin.readline

n, m, *v = map(int, open(0).read().split())
pSum, cnt = 0, [0] * m
for i in range(n):
    pSum = (pSum + v[i]) % m
    cnt[pSum] += 1
ans = 0
for i in range(m):
    if i == 0: ans += cnt[i] * (cnt[i] + 1) >> 1
    else: ans += cnt[i] * (cnt[i] - 1) >> 1
print(ans)