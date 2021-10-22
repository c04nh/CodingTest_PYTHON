# 1단계
# 폰켄몬

def solution(nums):
    answer = 0
    result = len(nums) / 2
    nums = set(nums)
    if len(nums) < result:
        answer = len(nums)
    else:
        answer = result
    return answer