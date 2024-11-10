# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
# move_l = ["l", "r", "u", "d"]

# # answer 리스트는 전역 변수로 사용되며, 이동 가능한 경로를 저장합니다.
# # solution 함수 내에서 매 호출 시마다 초기화되며, 필요한 경우 최종 답을 저장하게 됩니다.
# answer = "z"

# def check(x, y, n, m):
#     # 주어진 좌표 (x, y)가 격자 내에 있는지 확인하는 함수
#     return 1 <= x <= n and 1 <= y <= m

# def moving(result, k, move_n, x, y, r, c, n, m):
#     global answer  # 전역 변수 answer를 사용
#     if k < move_n + abs(x - r) + abs(y - c):
#         return
#     # 이동 횟수에 도달한 경우, 목표 지점에 도착했는지 확인
#     if k == move_n:
#         if x == r and y == c:
#             # 목표에 도달하면 answer 리스트에 경로(result)를 추가
#             answer=prev_s
#             return  # 이동 횟수 제한에 도달했으므로 종료
    
#     # 모든 방향으로 이동을 시도
#     for i, move in enumerate(moves):
#         mx, my = x + move[0], y + move[1]
#         if check(mx, my, n, m) and prev_s<answer:
#             # 이동 가능한 위치라면 다음 위치로 이동하여 DFS 탐색
#             moving(result + move_l[i], k + 1, move_n, mx, my, r, c, n, m)

# def solution(n, m, x, y, r, c, k):
#     global answer
#     answer = []  # answer 리스트 초기화 (새로운 함수 호출마다 초기화하여 이전 값 제거)
    
#     # DFS 탐색을 시작하여 경로 찾기
#     moving("", 0, k, x, y, r, c, n, m)
    
#     # 경로가 없는 경우 "impossible" 반환, 아니면 사전순 정렬 후 첫 번째 경로 반환
#     if not answer:
#         return "impossible"
#     else:
#         answer.sort()  # 사전순으로 정렬하여 가장 앞의 경로 선택
#         return answer[0]  # 사전순으로 가장 앞에 있는 경로 반환

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = "z"


def isVaild(nx, ny, n, m):
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    for i in range(4):
        if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer:
            dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s+dAlpha[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)

    return answer