"""
n,m=map(int,input().split())
w=[[1 for _ in range(m+1)] for _ in range(n)]
h=[[1 for _ in range(m)]  for _ in range(n+1)]
gongsa=int(input())

for i in range(gongsa):
	a,b,c,d=map(int,input().split())
	print(a,b,c,d)
	if abs(a-c)>0:
		print("가로 막힘")
		w[min(a,c)][b]=0
	elif abs(b-d)>0:
		print("세로 막힘")
		h[a][min(b,d)]=0

		
def DP(x,y):
	move_x=[1,0]
	move_y=[0,1]
	if x==n and y==n:
		return 1
	if w[x][y]!=0 or h[x][y]!=0:
		for (x_m,y_m) in move_x,move_y:
			return DP(x+x_m,y)+DP(x,y+y_m)
		
print(DP(0,0))
		

for row in w:
	print(row)
	print()
print()
for row in h:
	print(row)
	print()
"""
"""
n,m=map(int,input().split())
k=int(input())
dp=[[0] * (n+1) for _ in range(m+1)]
road=[]
dp[0][0]=1
for i in range(k):
	road.append(list(map(int,input().split())))
	
def check(current,a,b,c,d):
	if current==[a,b,c,d] or current==[c,d,a,b]:#다음위치 이동 여부
		return True
	else:
		return False

for x in range(m+1):
	for y in range(n+1):
		if y>0:
			for a,b,c,d in road:
				if check([y-1,x,y,x], a,b,c,d):
					break
			else:
				dp[x][y]+=dp[x][y-1]
		if x>0:
			for a,b,c,d in road:
				if check([y,x-1,y,x],a,b,c,d):
					break
			else:
				dp[x][y]+=dp[x-1][y]
print(dp)
print(dp[m][n])

"""









n,m=map(int,input().split())
k=int(input())
dp=[[0] * (n+1) for _ in range(m+1)]
road=[]
dp[0][0]=1

for _ in range(k):
	road.append(list(map(int,input().split())))
	

def check(current,a,b,c,d):
	if current==[a,b,c,d] or current==[c,d,a,b]:
		return True
	else:
		return False
	
	
for x in range(m+1):
	for y in range(n+1):
		if y>0:
			for a,b,c,d in road:
				if check([y-1,x,y,x],a,b,c,d):
					break
			else:
				dp[x][y]+=dp[x][y-1]
				
		if x>0:
			for a,b,c,d in road:
				if check([y,x-1,y,x],a,b,c,d):
					break
			else:
				dp[x][y]+=dp[x-1][y]
print(dp[-1][-1])
	













