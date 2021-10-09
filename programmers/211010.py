# 1단계
# 2016년

def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    count_day = 0
    count_day += sum(month[:a - 1])
    count_day += b
    answer = day[count_day % 7]
    return answer