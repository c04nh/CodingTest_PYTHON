# 1단계
# 숫자 문자열과 영단어

def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
    for i in num:
        s = s.replace(i, str(num.index(i)))
    answer = int(s)
    return answer