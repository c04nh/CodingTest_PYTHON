# 2단계
# 카펫

def solution(brown, yellow):
    answer = [0] * 2
    sum_num = brown + yellow
    for i in range(3, sum_num):
        j = sum_num // i
        if sum_num % i == 0 and j >= 3:
            col = max(i, j)
            row = min(i, j)
            center = (col - 2) * (row - 2)
            if center == yellow:
                answer[0] = col
                answer[1] = row
                return answer
    return answer