import sys
s=sys.stdin.readline().strip()

for i in range(len(s)):
	if s[i:]==s[i:][::-1]:#현재부터 뒤쪽까지, 한칸씩 가면서 뒤쪽부터 같은 지점을 찾음
		print(len(s)+i)
		break