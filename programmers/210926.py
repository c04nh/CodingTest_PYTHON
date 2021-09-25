# 1단계
# 제일 작은 수 제거하기

def solution(arr):
    answer = arr
    answer.remove(min(arr))
    if len(answer) == 0:
        answer.append(-1)
    return answer