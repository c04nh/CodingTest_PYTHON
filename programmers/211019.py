# 1단계
# 체육복

def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for a in set_reserve:
        if a - 1 in set_lost:
            set_lost.remove(a - 1)
        elif a + 1 in set_lost:
            set_lost.remove(a + 1)
    answer = n - len(set_lost)
    return answer