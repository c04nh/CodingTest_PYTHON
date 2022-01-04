# 더하기 사이클

N = int(input())
num = N
cnt = 0
while True:
    if cnt != 0 and N == num:
        break
    a = (num // 10) + (num % 10)
    num = (num % 10 * 10) + (a % 10)
    cnt += 1
print(cnt)