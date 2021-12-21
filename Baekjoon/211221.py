# 알람 시계

user_input = input()
arr = user_input.split(" ")
H = int(arr[0])
M = int(arr[1])
if M < 45:
    H -= 1
    M = 60 - (45 - M)
    if H < 0:
        H = 23
    print(H, end=" ")
    print(M)
else:
    print(H, end=" ")
    print(M - 45)