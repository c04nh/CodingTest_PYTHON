# 부녀회장이 될테야

APT = [[0 for a in range(15)] for a in range(15)]
for i in range(15):
    APT[i][1] = 1;
    APT[0][i] = i;
for i in range(1, 15):
    for j in range(2, 15):
        APT[i][j] = APT[i][j - 1] + APT[i - 1][j]
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(APT[k][n])