# 1단계
# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    L = 10
    R = 12
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            L = n
        elif n in [3, 6, 9]:
            answer += 'R'
            R = n
        else:
            n = 11 if n == 0 else n
            absL = abs(n - L)
            absR = abs(n - R)
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                R = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                L = n
            else:
                if hand == 'left':
                    answer += 'L'
                    L = n
                else:
                    answer += 'R'
                    R = n
    return answer