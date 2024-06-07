#다이나믹 프로그래밍
#자료구조 1차원
#복잡도 n
"""
go,small=map(int,input().split())
small_stones=[]
for _ in range(small):
	small_stones.append(int(input()))
dp=[0]*(go+1)
if go<3:
	print(1)

dp[0]=1
dp[1]=1
dp[2]=1


def check(now,jump):

	result=[True,True,True]
	if now+jump-1 in small_stones:
		result[0]
	if now+jump in small_stones:
		result[1]=False
	if now+jump+1 in small_stones:
		result[2]=False
	return result

jump=1

for i in range(2,go):
	result=[10000,10000,10000]
	if i in small_stones:
		break
	if (i+jump+1)>go:
		break
	else:
		move=check(i,jump)
		if move[0]==True:
			result[0]=dp[i-jump+1]
		if move[1]==True:
			dp[i]+=dp[i-jump]
		if move[2]==True:
			dp[i]+=dp[i-jump-1]
		print(i,"번째 계산",dp)
print(dp[-1])
	
"""
import math
from sys import stdin
N,stones_n=map(int,stdin.readline().split())

stone=set()
for _ in range(stones_n):
	stone.add(int(stdin.readline().rstrip()))
	
dp=[[10001]*(int(math.sqrt(2*N))+2) for _ in range(N+1)] #2차원 계산

dp[1][0]=0

for i in range(2,N+1):
	if i in stone:
		continue
	for v in range(1,int(math.sqrt(2*i)+1)): #
		dp[i][v]=min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1])+1

ans=min(dp[N])
if ans==10001:
	print(-1)
else:
	print(ans)
	
	
	