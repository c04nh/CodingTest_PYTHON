# 2단계
# 올바른 괄호

def solution(s):
    answer = True
    stack = []
    if s[0] == ')': return False
    for i in range(0, len(s)):
        if len(stack) != 0 and s[i] == ')':
            stack.pop()
        else:
            stack.append(s[i]);
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer