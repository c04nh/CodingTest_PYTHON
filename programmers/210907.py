# 1단계
# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    for a in range(len(seoul)):
        if seoul[a] == "Kim":
            answer = f'김서방은 {a}에 있다'
    return answer