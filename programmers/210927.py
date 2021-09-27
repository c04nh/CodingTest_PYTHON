# 1단계
# 정수 제곱근 판별

import math

def solution(n):
    num = math.sqrt(n)
    if num % int(num) > 0:
        answer = -1
    else:
        answer = (num + 1) * (num + 1)
    return answer