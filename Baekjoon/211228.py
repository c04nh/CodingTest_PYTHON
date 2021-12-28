# A+B - 7

num = int(input())
for a in range(1, num + 1):
    user_input = input()
    arr = user_input.split(' ')
    A = int(arr[0])
    B = int(arr[1])
    print(f'Case #{a}: {A + B}')