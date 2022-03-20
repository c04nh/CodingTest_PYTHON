# 파도반 수열

seq = [0] * 101
seq[1] = 1
seq[2] = 1
seq[3] = 1
for i in range(0, 98):
    seq[i + 3] = seq[i] + seq[i + 1]
T = int(input())
for i in range(T):
    N = int(input())
    print(seq[N])