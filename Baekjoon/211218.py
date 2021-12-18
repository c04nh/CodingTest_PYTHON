# 시험 성적

num = int(input())
if num >= 90:
    score = 'A'
elif num >= 80:
    score = 'B'
elif num >= 70:
    score = 'C'
elif num >= 60:
    score = 'D'
else:
    score = 'F'
print(score)