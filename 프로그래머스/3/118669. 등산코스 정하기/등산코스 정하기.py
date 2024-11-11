# # Max_size=100000
# # minimum=Max_size
# # reached_min=0
# # reached=0
    
# # def move(i,j,summits,intensity,reach,max_moves,n,moves):
    
# #     #i=현재 지점
# #     #j=스타트지점
# #     #gates=정상인가?
# #     #intensity=최대로 못 쉰 시간
# #     #reach=정상 도착 여부
# #     #max_moves=최대 이동거리, 너무 길어지면 종료
# #     #moves=이동가능여부 확인
# #     global reached
# #     # if max_moves>n:#너무 많이 가면
# #     #     print("터짐")
# #     #     return 
# #     if i in summits:#봉우리 도착하면
# #         reach=True  
# #         reached=i
# #         print("봉우리도착")
# #     if i==j and reach==True:#봉우리 지나고, 원래 입구로 도착하면
# #         print("입구 도착")
# #         return [reached,min(intensity,minimum)]
# #     else:#아직 이동중이면(봉우리 도착, 도착x 둘다 )
# #         for j in range(n):#다음으로 이동
# #             print(j,"다음으로 이동?")
# #             if moves[i][j] != False:#이동 가능하면 이동
# #                 print(j,"다음으로 이동")
# #                 max_moves+=1 #이동횟수 +1
# #                 move(i,j,summits,max(intensity,moves[i][j]),reach,max_moves,n,moves)#다음으로 이동
                
# #     return [reached,min(intensity,minimum)]


# # def solution(n, paths, gates, summits):
# #     #n=방문 가능 장소 갯수
# #     #paths=지점 i, j와 시간 w
# #     #gates=게이트 번호
# #     #summits=산봉우리 번호
# #     answer = [10000000,1000000]
# #     temp=[]
# #     moves=[[False for _ in range(n+1)] for _ in range(n+1)]
# #     for i,j,w in paths:
# #         moves[i][j]=w
# #         moves[j][i]=w
         
# #     for start in gates:#각 스타트 지점별로 이동 시작
# #         temp=move(start,start,summits,Max_size,False,0,n,moves)
# #         answer=min(temp,answer)
# #     answer=temp
    
# #     return answer


# from collections import defaultdict
# from heapq import heappop,heappush

# def solution(n,paths,gates,summits):
#     summits.sort()
#     summit_set=set(summits)
#     graph=defaultdict(list)#디폴트 딕트로 시작점에 대해 가중치, 이동경로 저장
#     for i,j,w in paths: #주어진 경로 정보를 추가함
#         graph[i].append((w,j)) 
#         graph[j].append((w,i))
        
#     def get_min_intensity():
#         pq=[] #intensity, 현재위치
#         visited=[1000000]*(n+1) #각 노드 방문별로 길이지정
        
#         for gate in gates:
#             heappush(pq,(0,gate)) #각 입구에 대한 길이랑 번호 지정
#             visited[gate]=0 #게이트 입구는 0으로 지정
            
#         while pq:
#             intensity,node=heappop(pq)# 현재 위치에 대해서 확인
            
#             if node in summits or intensity>visited[node]:#산봉우리 도착 또는 현재 위치보다 크면 이동x
#                 continue
                
#             for weight, next_node in graph[node]: #이동 가능한 위치로 이동 케이스
#                 new_intensity=max(intensity,weight) #현재꺼랑 다음꺼랑 비교해서 큰걸로 집어넣음
#                 if new_intensity<visited[next_node]: #비교 및 교체
#                     visited[next_node]=new_intensity 
#                     heappush(pq,(new_intensity,next_node))#최소 경로를 계속 집어넣음
#         min_intensity=[0,10000000]
#         for summit in summits: #각 정상 위치에 대해서 최솟값 계산
#             if visited[summit]<min_intensity[1]:
#                 min_intensity[0]=summit
#                 min_intensity[1]=visited[summit]
#         return min_intensity

    
#     return get_min_intensity()
from collections import defaultdict
from heapq import heappop, heappush


# n: 노드 수
# gates: 출입구, sumits: 산봉우리
def solution(n, paths, gates, summits):
    def get_min_intensity():
        pq = []  # (intensity, 현재 위치)
        visited = [10000001] * (n + 1)

        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate] = 0

        # 산봉우리에 도착할 때까지 반복
        while pq:
            intensity, node = heappop(pq)

            # 산봉우리이거나 더 큰 intensity라면 더 이상 이동하지 않음
            if node in summits_set or intensity > visited[node]:
                continue

            # 이번 위치에서 이동할 수 있는 곳으로 이동
            for weight, next_node in graph[node]:
                # next_node 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
                # (출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음)
                new_intensity = max(intensity, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq, (new_intensity, next_node))

        # 구한 intensity 중 가장 작은 값 반환
        min_intensity = [0, 10000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]

        return min_intensity

    summits.sort()
    summits_set = set(summits)
    # graph: 등산로 정보
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return get_min_intensity()