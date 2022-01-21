# 다이얼

s = input()
cnt = 0
for i in s:
    if ord(i) < 68: cnt += 3
    elif ord(i) < 71: cnt += 4
    elif ord(i) < 74: cnt += 5
    elif ord(i) < 77: cnt += 6
    elif ord(i) < 80: cnt += 7
    elif ord(i) < 84: cnt += 8
    elif ord(i) < 87: cnt += 9
    else: cnt += 10
print(cnt)