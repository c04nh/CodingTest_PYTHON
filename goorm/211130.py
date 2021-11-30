# 1단계
# 태민이의 취미

user_input = input()
num = int(user_input)
sum = num * (num + 1) // 2 % 1000000007
result = sum * sum % 1000000007
print(result)