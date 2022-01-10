# 평균은 넘겠지

num = int(input())
for a in range(num):
    arr = []
    user_input = input()
    arr1 = user_input.split(' ')
    n = int(arr1[0])
    for b in range(n):
        arr.append(int(arr1[b + 1]))
    sum_num = sum(arr)
    avg = sum_num / n
    cnt = 0
    for item in arr:
        if item > avg:
            cnt += 1
    print(f'{cnt / n * 100:.3f}%')