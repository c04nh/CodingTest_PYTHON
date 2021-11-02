# 1단계
# 369 게임

user_input = input()
clap = 0
for a in range(1, int(user_input)):
	clap += str(a).count("3") + str(a).count("6") + str(a).count("9")
print(clap)
