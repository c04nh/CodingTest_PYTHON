# 1단계
# K번째수

def solution(array, commands):
    answer = []
    for a in commands:
        arr = []
        i = a[0] - 1
        j = a[1] - 1
        k = a[2] - 1
        for b in range(i, j + 1):
            arr.append(array[b])
        arr.sort()
        answer.append(arr[k])

    return answer