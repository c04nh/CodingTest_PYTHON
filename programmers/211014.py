# 1단계
# 모의고사

def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for a in range(len(answers)):
        if answers[a] == s1[a % 5]:
            cnt1 += 1
        if answers[a] == s2[a % 8]:
            cnt2 += 1
        if answers[a] == s3[a % 10]:
            cnt3 += 1
    max_score = max(cnt1, cnt2, cnt3)
    if(max_score == cnt1):
        answer.append(1)
    if(max_score == cnt2):
        answer.append(2)
    if(max_score == cnt3):
        answer.append(3)
    return answer