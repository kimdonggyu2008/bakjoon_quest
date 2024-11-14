

def solution(routes):
    # routes 정렬? 가장 앞부터 추가하기
    # 만약에 cameras의 데이터 중에 현재 데이터가 포함이 안되면, 새로 추가?
    # 있으면 냅두기?
    answer = 0
    routes.sort()
    #print(dir(routes))
    #print(routes)
    count=1
    start,end=routes[0][0],routes[0][1]
    print(start,end)
    for route in routes:
        #if start<=route[0]<=end or start<=route[1]<=end:
        #    continue
        if end<route[0]:
            count+=1
            end=route[1]
        else:
            end=min(end,route[1])
    return count