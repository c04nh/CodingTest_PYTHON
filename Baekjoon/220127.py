# 분수찾기

X = int(input())
cnt = 1
sum = 0
while True:
    if X <= (sum + cnt):
        if cnt % 2 == 1:
            print(f'{cnt - (X - sum - 1)}/{X - sum}')
            break
        else:
            print(f'{X - sum}/{cnt - (X - sum - 1)}')
            break
    else:
        sum += cnt
        cnt += 1