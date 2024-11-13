from collections import deque

# def bfs(graph, node, visited):
#     queue=deque([node])
#     visited[node]=True
#     sheep=0
#     wolf=0
#     while queue:
#         v=queue.popleft()
#         for i in graph[v]:
#             if not visited[i] and 0<wolf<sheep:
#                 if info[i] == 0:
#                     sheep+=1
                    
#                 if info[i]==1:
#                     wolf+=1 
                    
#                 queue.append(i)
#                 visited[i]=True
#             print("이동함")
            
            
def solution(info, edges):
    answer = []
    visited=[0]*len(info)
    
    def dfs(sheep,wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        
        for p,c in edges:#현재 위치 기준으로 이동
            if visited[p] and not visited[c]: #다음 위치 방문 안했을 때
                visited[c]=1# 방문 처리
                if info[c]==0: #양
                    dfs(sheep+1,wolf)
                else: #늑대
                    dfs(sheep,wolf+1)
                visited[c]=0
                
    visited[0]=1
    dfs(1,0)
    return max(answer)