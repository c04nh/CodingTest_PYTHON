# 서로 다른 부분 문자열의 개수

N = input()
ans = set()
for i in range(len(N)):
    for j in range(i, len(N)):
        tmp = N[i:j+1]
        ans.add(tmp)
print(len(ans))