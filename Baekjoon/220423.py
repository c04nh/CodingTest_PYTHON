# 제로

N = int(input())
Z = []
for i in range(N):
    num = int(input())
    if num == 0:
        Z.pop()
    else:
        Z.append(num)
print(sum(Z))