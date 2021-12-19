# 윤년

num = int(input())
tf = 0
if num % 4 == 0:
    if num % 100 != 0 or num % 400 == 0:
        tf = 1
print(tf)