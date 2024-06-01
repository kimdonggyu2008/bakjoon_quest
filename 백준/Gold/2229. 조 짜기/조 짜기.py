person=int(input())
points=list(map(int,input().split()))

"""
def DP(points,index):
	if index==0:
		return points[0]
	else:
		case1=max(DP(points,index-1)+points[index],points[index])#ㅈ자르는 경우
		case2=max(DP(points,index-1),points[index])# 안자르는 경우
		return max(case1,case2)
"""
dp=[0 for _ in range(person+1)] #자료구조 활용

for i in range(person+1):
	max_val=-10000
	min_val=100000
	for k in range(i, 0, -1): 
		max_val=max(max_val,points[k-1]) # 새로운 사람이 포함되어 구성될 수 있는 팀의 점수
		min_val=min(min_val,points[k-1])
		dp[i] = max(max_val-min_val+dp[k-1], dp[i])

print(dp[person])
	
