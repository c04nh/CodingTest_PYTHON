# 한수

num = int(input())
cnt = 0
for a in range(1, num + 1):
    if a <= 99:
        cnt += 1
    else:
        str_num = str(a)
        if int(str_num[1]) - int(str_num[0]) == int(str_num[2]) - int(str_num[1]):
            cnt += 1
print(cnt)
