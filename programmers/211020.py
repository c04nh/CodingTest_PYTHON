# 1단계
# 예산

def solution(d, budget):
    answer = 0
    d.sort()
    for a in d:
        if budget - a >= 0:
            budget -= a
            answer += 1
        else:
            break
    return answer