# 팩토리얼 0의 개수

num = int(input())
cnt = 0
while num >= 5:
    cnt += num // 5
    num //= 5
print(cnt)