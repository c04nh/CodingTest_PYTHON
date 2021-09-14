# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if x != y:
                answer.append(numbers[x] + numbers[y])
    return sorted(list(set(answer)))