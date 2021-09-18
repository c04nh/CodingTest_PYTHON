# 음양 더하기

def solution(absolutes, signs):
    sum_num = 0
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] = absolutes[i] * -1
        sum_num += absolutes[i]
    return sum_num