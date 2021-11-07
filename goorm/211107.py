# 1단계
# 네 수의 곱

def mul(a, b):
    return a * b

user_input = input()
arr = user_input.split(" ")
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])
print(mul(mul(a, b), mul(c, d)))