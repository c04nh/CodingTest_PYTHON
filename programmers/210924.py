# 1단계
# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    big = max(n, m)
    small = min(n, m)
    max_num = 0
    min_num = 0
    for i in range(1, small + 1):
        if n % i == 0 and m % i == 0:
            max_num = i
    answer.append(max_num)
    for i in range(1, big + 1):
        if n * i % m == 0:
            min_num = n * i
            break
    answer.append(min_num)
    return answer