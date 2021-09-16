# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        count_num = 0
        for y in range(1, x + 1):
            if x % y == 0:
                count_num += 1
        if count_num % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer