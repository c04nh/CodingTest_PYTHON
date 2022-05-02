# 2단계
# 124 나라의 숫자

def solution(n):
    numbers = ["4", "1", "2"]
    answer = ''
    num = n
    while num > 0:
        remainder = num % 3
        num //= 3
        if remainder == 0:
            num -= 1
        answer = numbers[remainder] + answer
    return answer