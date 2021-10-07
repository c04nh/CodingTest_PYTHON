# 1단계
# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    for a in range(10):
        if a not in numbers:
            answer += a
    return answer