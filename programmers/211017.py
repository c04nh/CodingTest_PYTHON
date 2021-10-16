# 1단계
# 3진법 뒤집기

def solution(n):
    answer = 0
    result = ''
    while True:
        result += str(int(n % 3))
        n /= 3
        if n < 1:
            break
    squared = len(result) - 1
    for a in result:
        answer += int(a) * (3 ** squared)
        squared -= 1
    return answer