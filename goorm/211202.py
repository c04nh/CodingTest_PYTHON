# 1단계
# 서울에서 경산까지

user_input = input()
arr = user_input.split(' ')
num = int(arr[0])
K = int(arr[1])
travel = []
for a in range(num):
	user_input1 = input()
	arr1 = user_input1.split(' ')
	array = []
	array.append(int(arr1[0]))
	array.append(int(arr1[1]))
	array.append(int(arr1[2]))
	array.append(int(arr1[3]))
	travel.append(array)
n = len(travel)
memo = [[0 for _ in range(K+1)] for _ in range(n+1)]
for i in range(1, n+1):
	t_walk, v_walk, t_bike, v_bike = travel[i-1]
	for j in range(K+1):
		walk = memo[i-1][j-t_walk]+v_walk if j>=t_walk and memo[i-1][j-t_walk]!=-1 else -1
		bike = memo[i-1][j-t_bike]+v_bike if j>=t_bike and memo[i-1][j-t_bike]!=-1 else -1
		memo[i][j]=max(walk, bike)
print(memo[n][K])
