# 1단계
# 소수 만들기

def solution(nums):
    answer = 0
    for a in range(len(nums) - 2):
        for b in range(a + 1, len(nums) - 1):
            for c in range(b + 1, len(nums)):
                sum_num = 0
                sum_num += nums[a] + nums[b] + nums[c]
                count_num = 0
                for d in range(1, sum_num + 1):
                    if sum_num % d == 0:
                        count_num += 1
                if count_num == 2:
                    answer += 1

    return answer