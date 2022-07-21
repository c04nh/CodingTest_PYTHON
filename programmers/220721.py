# 미림 마이스터고 코딩테스트 대비반 (Python)
# 07. 깊이/너비 우선 탐색(DFS/BFS) 대표 문제 풀이
# 여행경로

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer