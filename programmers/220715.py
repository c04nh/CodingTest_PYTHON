# 미림 마이스터고 코딩테스트 대비반 (Python)
# 03. 정렬(Sort) 대표 문제 풀이
# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))