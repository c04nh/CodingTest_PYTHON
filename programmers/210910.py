# 1단계
# 문자열 내 p와 y의 개수

def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')

    if p == y:
        return True
    else:
        return False