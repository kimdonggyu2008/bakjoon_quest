"""
n,k=map(int, input().split(" "))

ws=[]
vs=[]
for _ in range(n):
	w,v=map(int,input().split(" "))
	ws.append(w)#가치
	vs.append(v)#무게
	
	
def knapsack2(i,W,w,p):
	if i<=0 or W<=0: #최대 길이, 무게 최대
		return 0
	if w[i]>W:#그냥 넘는 경우 넘김
		value=knapsack2(i-1,W,w,p)
		return value
	else:
		left=knapsack2(i-1,W,w,p)#안 빼는 경우
		right=knapsack2(i-1,W-w[i],w,p)#빼는 경우
		return max(left,p[i]+right)
	

print(knapsack2(n-1,k,ws,vs))
"""
n, k = map(int, input().split())

stuff = [[0, 0]]
for _ in range(n):
    stuff.append(list(map(int, input().split()))) # [weight, value]

knapsack = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1): # 탐색할 물건의 인덱스
    for j in range(1, k+1): # 현재 넣을 수 있는 최대 무게
        weight = stuff[i][0]
        value = stuff[i][1]

        if weight > j: # 탐색하는 물건의 무게가 최대 배낭 무게를 초과할 경우
            knapsack[i][j] = knapsack[i-1][j] # 이전 가치 유지
        else: # 탐색하는 물건의 무게가 최대 배낭 무게를 초과하지 않을 경우
        	# 1) 넣지 않기 -> 이전 가치 유지
            # 2) 넣기 -> 탐색하는 물건의 가치 + 현재 넣을 물건을 제외하고 탐색하는 물건의 무게를 뺀 무게를 최대 무게로 설정했을 때의 최대 가치
            knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])

print(knapsack[n][k])