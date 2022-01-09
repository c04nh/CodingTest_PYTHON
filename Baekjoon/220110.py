# OX문제

num = int(input())
arr = []
for a in range(num):
    arr.append(input())
for a in arr:
    result = 0
    score = 0
    for b in a:
        if b == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)