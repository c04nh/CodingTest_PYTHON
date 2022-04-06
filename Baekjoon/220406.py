# 주유소

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
minCost = cost[0]
sum = 0
for i in range(N - 1):
    if minCost > cost[i]:
        minCost = cost[i]
    sum += (minCost * dist[i])
print(sum)