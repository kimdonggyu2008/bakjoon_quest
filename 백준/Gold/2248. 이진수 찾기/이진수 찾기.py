n,l,k=map(int,input().split())

numbers=[ [0]*n for _ in range(n)]
numbers[0][0]=1

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            numbers[i][j] = numbers[i-1][j]  # 첫 번째 열은 바로 위 값으로 설정
        else:
            numbers[i][j] = numbers[i-1][j] + numbers[i-1][j-1]

result=""
for i in reversed(range(n)):
	if k>sum(numbers[i][:l+1]):
		result+="1"
		k-=sum(numbers[i][:l+1])
		l-=1
	else:
		result+="0"
	
	
# if len(result)<n:
# 	for i in range(n-len(result)):
# 		result+="0"
# result = ''.join(reversed(result))
print(result)
	