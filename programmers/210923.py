# 1단계
# 콜라츠 추측

def solution(num):
    answer = 0
    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num = num / 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
        if answer == 500 and num != 1:
            answer = -1
            break
    return answer