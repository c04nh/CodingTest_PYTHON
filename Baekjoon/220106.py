# 최댓값

arr = []
for a in range(9):
    arr.append(int(input()))
max_num = max(arr)
index = arr.index(max_num) + 1
print(max_num)
print(index)