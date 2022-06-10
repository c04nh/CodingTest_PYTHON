# 2단계
# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for scov in scoville:
        heapq.heappush(heap, scov)

    while heap[0] < K:
        if len(heap) == 1: return -1
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1

    return answer