# 1단계
# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a, b in zip(participant, completion):
        if a != b:
            return a

    return participant[-1]