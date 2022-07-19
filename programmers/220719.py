# 미림 마이스터고 코딩테스트 대비반 (Python)
# 05. 힙(Heap) 대표 문제 풀이
# 더 맵게

from heapq import *

def solution(scoville, K):
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= K else -1