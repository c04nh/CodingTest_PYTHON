# 1단계
# 약수 구하기

user_input = input()
user_input = int(user_input)
for a in range(1, user_input + 1):
    if user_input % a == 0:
        print(f'{a} ', end="")
