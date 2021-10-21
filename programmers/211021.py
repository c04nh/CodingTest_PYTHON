# 1단계
# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        num = str(bin(i | j)[2:])
        num = num.rjust(n, '0')
        num = num.replace('1', '#')
        num = num.replace('0', ' ')
        answer.append(num)
    return answer