# 1단계
# 실패율

def solution(N, stages):
    answer = {}
    user = len(stages)
    for i in range(1, N+1):
        if user != 0:
            count_user = stages.count(i)
            answer[i] = count_user / user
            user -= count_user
        else:
            answer[i] = 0
    answer = sorted(answer, key=lambda x : answer[x], reverse=True)
    return answer