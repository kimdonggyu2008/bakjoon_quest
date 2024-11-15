import heapq

def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return 0
    works=[-i for i in works]
    heapq.heapify(works)
    
    for i in range(n): #가장 많은 경우를 고르고 계속 1씩 뺌
        work=heapq.heappop(works)
        work+=1
        heapq.heappush(works,work)
    
    return sum(i**2 for i in works)