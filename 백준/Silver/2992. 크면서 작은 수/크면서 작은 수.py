X=input()
number=""
minnumber="999999"
used=[False] * len(X)

def backtrack(depth):
	global number
	global minnumber
	
	if depth==len(X): #주어진 값, 현재 가장 작은 수보다 작은경우
		if X<number<minnumber:
			minnumber=number
		return
	
	for i in range(len(X)):
		if used[i]==True:
			continue
		used[i]=True
		number+=X[i]
		backtrack(depth+1)
		used[i]=False
		number=number[:-1]
			
backtrack(0)

if minnumber=="999999":
	minnumber=0
print(minnumber)