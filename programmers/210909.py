# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    list_s = (sorted(s, reverse=True))
    for a in list_s:
        answer += a
    return answer