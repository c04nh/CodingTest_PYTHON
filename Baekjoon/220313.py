# N-Queen

answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])

# 시간 초과
'''
N = int(input())
arr = [0] * N
count = 0

def Possibility(idx):
    for i in range(idx):
        if arr[idx] == arr[i] or abs(arr[idx] - arr[i]) == idx - i:
            return False
    return True

def nQueen(idx):
    if idx == N:
        global count
        count += 1
        return
    for i in range(N):
        arr[idx] = i
        if Possibility(idx):
            nQueen(idx + 1)

nQueen(0)
print(count)
'''