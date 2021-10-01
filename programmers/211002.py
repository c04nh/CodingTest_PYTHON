# 1단계
# 시저 암호

def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if 65 <= ord(i) <= 90:
                if 91 <= ord(i) + n:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > 122:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
    return answer