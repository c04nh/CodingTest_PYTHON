# 1단계
# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if a < b:
        for x in range(a, b + 1):
            answer += x
    elif a > b:
        for x in range(b, a + 1):
            answer += x
    else:
        return a
    return answer