# 미림 마이스터고 코딩테스트 대비반 (Python)
# 04. 탐욕법(Greedy) 대표 문제 풀이
# 큰 수 만들기

def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)