# 1단계
# 자연수 뒤집어 배열로 만들기

def solution(n):
    n = str(n)
    answer = list(n)
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer