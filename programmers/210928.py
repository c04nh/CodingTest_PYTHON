# 1단계
# 정수 내림차순으로 배치하기

def solution(n):
    n = str(n)
    sort_n = sorted(n, reverse=True)
    answer = ""
    for i in sort_n:
        answer += i
    answer = int(answer)
    return answer