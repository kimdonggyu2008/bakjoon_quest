import sys

answer=[]
while True:
	stack=[]
	count=0
	s=sys.stdin.readline()
	if '-' in s:
		break
	for i in range(len(s)): #각 길이에 대해서
		if not stack and s[i] == '}': #스텍 빔, 현재위치가 }
			count += 1 #역순이라 +1
			stack.append('{') #반대꺼 추가
		elif stack and s[i] == '}': #스텍에 {이 1개 이상 있음
			stack.pop() #한개 날림
		else:
			stack.append(s[i]) # }가 들어가서 남음
	count+=len(stack)//2 #역순으로 남은 경우의 절반 만큼 돌려야함
	answer.append(count)
for i in range(len(answer)):
	print(i+1,". ",answer[i],sep="")
		
	
			
	