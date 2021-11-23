# 1단계
# 헷갈리는 작대기

user_input = input()
cnt = [0, 0, 0, 0]
cnt[0] = user_input.count('1')
cnt[1] = user_input.count('I')
cnt[2] = user_input.count('l')
cnt[3] = user_input.count('|')
for a in cnt:
	print(a)