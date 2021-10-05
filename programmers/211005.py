# 1단계
# 1주차_부족한 금액 계산하기

def solution(price, money, count):
    final_price = 0
    for i in range(1, count + 1):
        final_price += price * i
    answer = final_price - money
    if answer <= 0:
        answer = 0
    return answer