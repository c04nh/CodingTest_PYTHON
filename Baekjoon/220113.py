# 셀프 넘버

arr = list(range(1, 10_001))
remove_list = []
for num in arr:
    for n in str(num):
        num += int(n)
    if num <= 10_000:
        remove_list.append(num)

for remove_num in set(remove_list):
    arr.remove(remove_num)
for num in arr:
    print(num)