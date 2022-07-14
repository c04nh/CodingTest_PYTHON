# 미림 마이스터고 코딩테스트 대비반 (Python)
# 02. 탐욕법(Greedy) 대표 문제 풀이
# 체육복

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for reserve_person in reserve_set:
        if reserve_person - 1 in lost_set:
            lost_set.remove(reserve_person - 1)
        elif reserve_person + 1 in lost_set:
            lost_set.remove(reserve_person + 1)

    return n - len(lost_set)
