# 1단계
# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    for x in range(1, len(arr)):
        if arr[x] != arr[x-1]:
            answer.append(arr[x])
    return answer