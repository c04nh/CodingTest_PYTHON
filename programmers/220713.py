# 미림 마이스터고 코딩테스트 대비반 (Python)
# 01. 해시(Hash) 대표 문제 풀이
# 완주하지 못한 선수

import collections

def solution(participant, completion):
    answer =  list((collections.Counter(participant) - collections.Counter(completion)).keys())[0]
    return answer
