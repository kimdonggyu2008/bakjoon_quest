
def solution(n, s):
    answer = []
    ttemp=[]
    hae=s//n
    nameo=s%n
    for i in range(n):
        answer.append(hae)
    for i in range(nameo):
        answer[i]+=1
    if n>s:
        return [-1]
    answer.sort()
    return answer