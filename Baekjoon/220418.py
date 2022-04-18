# 조합 0의 개수

def five_power_n(num):
    cnt = 0
    while num >= 5:
        cnt += num // 5
        num //= 5
    return cnt


def two_power_n(num):
    cnt = 0
    while num >= 2:
        cnt += num // 2
        num //= 2
    return cnt


N, M = map(int, input().split())
cnt5 = five_power_n(N) - five_power_n(N - M) - five_power_n(M)
cnt2 = two_power_n(N) - two_power_n(N - M) - two_power_n(M)
print(min(cnt5, cnt2))