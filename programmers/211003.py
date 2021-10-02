# 1단계
# 소수 찾기

def solution(n):
    num = set(range(2, n + 1))

    for a in range(2, n + 1):
        if a in num:
            num -= set(range(a * 2, n + 1, a))
    answer = len(num)
    return answer