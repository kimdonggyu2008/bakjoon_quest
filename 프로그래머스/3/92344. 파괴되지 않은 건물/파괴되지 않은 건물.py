def solution(board, skill):
    # answer = 0
    #브루트 포스
    # tuntun=board
    # for type, r1,c1,r2,c2, degree in skill:
    #     if type==1:
    #         for i in range(r1,r2+1):
    #             for j in range(c1,c2+1):
    #                 tuntun[i][j]-=degree
    #     elif type==2:
    #         for i in range(r1,r2+1):
    #             for j in range(c1,c2+1):
    #                 tuntun[i][j]+=degree
    # for row in tuntun:
    #     for data in row:
    #         if data>0:
    #             answer+=1
    #누적합
    n,m,cnt=len(board),len(board[0]),0
    accumulate_sum=[[0 for _ in range(m+1)] for __ in range(n+1)]
    for attack_type,y1,x1,y2,x2,degree in skill:
        val= -degree if attack_type==1 else degree
        accumulate_sum[y1][x1]+=val
        accumulate_sum[y2+1][x2+1]+=val
        accumulate_sum[y1][x2+1]-=val
        accumulate_sum[y2+1][x1]-=val
    for i in range(n+1):
        for j in range(m):
            accumulate_sum[i][j+1]+=accumulate_sum[i][j]
            
    for j in range(m+1):
        for i in range(n):
            accumulate_sum[i+1][j]+=accumulate_sum[i][j]
    return sum([1 for i in range(n) for j in range(m) if board[i][j]+accumulate_sum[i][j]>0])