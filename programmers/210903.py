# 1단계
# 평균 구하기

def solution(arr):
    answer = 0
    for a in arr:
        answer += a
    return answer / len(arr)