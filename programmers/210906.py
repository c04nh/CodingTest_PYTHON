# 1단계
# 수박수박수박수박수박수?

def solution(n):
    answer = ''
    for x in range(1, n+1):
        if x % 2 == 1:
            answer += '수'
        else:
            answer += '박'
    return answer