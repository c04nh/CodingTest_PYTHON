# 1단계
# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        tmp = []
        for y in range(len(arr1[x])):
            tmp.append(arr1[x][y] + arr2[x][y])
        answer.append(tmp)
    return answer