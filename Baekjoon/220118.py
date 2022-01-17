# 문자열 반복

T = int(input())
for i in range(T):
    user_input = input()
    arr = user_input.split(' ')
    R = int(arr[0])
    S = arr[1]
    for j in S:
        for k in range(R):
            print(j, end='')
    print()