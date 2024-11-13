# from collections import deque

# def bfs(x,y,graph):
#     dx=[0,1,0,-1]
#     dy=[1,0,-1,0]
#     result=[]
#     queue=deque([(x,y,0,1,0,0),(x,y,1,0,0,0)])#현재 위치,이전 방향, 몇칸 이동, 몇번 꺾었나 정보
#     visited=set([(x,y)])#현재 위치 방문 여부
#     while queue:
#         move_x,move_y,before_x,before_y,moves,moves_kkeok=queue.popleft()#현재 위치에 대해 하나씩 빼고 이동 가능한 위치로 이동
#         print(move_x,move_y,before_x,before_y,moves,moves_kkeok)
#         if move_x==len(graph)-1 and move_y==len(graph)-1: #도착한 경우들
#             print(move_x,move_y)
#             result.append([moves,moves_kkeok])
#             continue
#         for i in range(4): #현재 위치에 대해서 4방향으로 찾아봄
#             nx=move_x+dx[i]
#             ny=move_y+dy[i]
            
#             if 0<=nx<len(graph) and 0<=ny<len(graph) and graph[nx][ny]==0:#이동 가능한 경우
#                 #print("이동 가능한 방향",dx[i],dy[i])
            
#                 if (nx,ny) not in visited:
#                     #print("방문 하러감",nx,ny)
#                     if dx[i]!=before_x and dy[i]!=before_y:#방향이 달라진 경우
#                         #print("방향 업데이트")
#                         moves_kkeok+=1 #꺾임 1 추가
#                         before_x=dx[i] #방향 업데이트
#                         before_y=dy[i]
#                     visited.add((nx,ny))
#                     queue.append((nx,ny,before_x,before_y,moves+1,moves_kkeok))
#         print(queue)
            
                
#     return result


# def solution(board):
#     # len*len 모양의 장판
#     # 최우선은 우, 하, 좌, 상 
    
#     answer=bfs(0,0,board)
#     minimum=100000000
#     #print(answer)
#     for data in answer:
#         minimum=min(minimum,(data[0]*100)+(data[1]*500))
#     print(minimum)
#     return minimum

from heapq import heappop,heappush
from sys import maxsize

def solution(board):
    N=len(board)
    costBoard = [[ [maxsize] * N for _ in range(N) ] for _ in range(4)]
    for i in range(4):
        costBoard[i][0][0]=0
    heap=[(0,0,0,0),(0,0,0,2)]
    while heap:
        cost,x,y,d=heappop(heap)
        for dx,dy,dd in ((1,0,0),(-1,0,-1),(0,1,2),(0,-1,3)):
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=N or ny<0 or ny>=N or board[ny][nx]:
                continue
            newCost=cost+(100 if d==dd else 600)
            
            if costBoard[dd][ny][nx]>newCost:
                costBoard[dd][ny][nx]=newCost
                heappush(heap,(newCost,nx,ny,dd))
    return min(costBoard[0][N-1][N-1], costBoard[1][N-1][N-1], costBoard[2][N-1][N-1], costBoard[3][N-1][N-1])
