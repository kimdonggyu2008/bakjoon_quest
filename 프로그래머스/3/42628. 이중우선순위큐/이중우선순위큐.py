import heapq

def solution(operations):
    answer = []
    min_heap=[]
    max_heap=[]
    for command in operations:
        com,number=list(map(str,command.split()))
        number=int(number)
        if com=="I":
            heapq.heappush(min_heap,number)
            heapq.heappush(max_heap,-number)
        elif com=="D" and number==1:#최댓값 삭제
            if len(max_heap)!=0:
                max_data=heapq.heappop(max_heap)
                min_heap.remove(-max_data)
        elif com=="D" and number==-1:
            if len(min_heap)!=0:
                min_data=heapq.heappop(min_heap)
                max_heap.remove(-min_data)
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
    if min_heap:
        answer=[-heapq.heappop(max_heap),heapq.heappop(min_heap)]
    else:
        answer=[0,0]
            
    
    return answer