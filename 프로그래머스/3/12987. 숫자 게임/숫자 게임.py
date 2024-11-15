import heapq
import math
def solution(A, B):
    answer = 0 #바로 위 값을 계속 찾아야 함
    A=sorted(A,reverse=True)# 카운터로 갯수 세고, 
    B=sorted(B,reverse=True)
    i=0
    for a in A:
        if a<B[i]:
            answer+=1
            i+=1
      
    return answer