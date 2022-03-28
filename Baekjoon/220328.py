# 가장 긴 바이토닉 부분 수열

N = int(input())
case = list(map(int, input().split()))
reverse_case = case[::-1]
increase = [1 for i in range(N)]
decrease = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
result = [0 for i in range(N)]
for i in range(N):
    result[i] = increase[i] + decrease[N - i - 1] -1
print(max(result))