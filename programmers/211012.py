# 1단계
# 로또 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    count_zero = lottos.count(0)
    count_num = 0
    for a in lottos:
        if a in win_nums:
            count_num += 1
    highest = count_num + count_zero
    for a in [highest, count_num]:
        if a == 6:
            answer.append(1)
        elif a == 5:
            answer.append(2)
        elif a == 4:
            answer.append(3)
        elif a == 3:
            answer.append(4)
        elif a == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer