# 1단계
# 가위바위보

user_input = input()
arr = user_input.split(' ')
cnt = [arr.count('1'), arr.count('2'), arr.count('3')]
if cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0:
	print(0)
elif cnt[0] == 5 or cnt[1] == 5 or cnt[2] == 5:
	print(0)
elif cnt[0] == 0:
	print(cnt[2])
elif cnt[1] == 0:
	print(cnt[0])
else:
	print(cnt[1])