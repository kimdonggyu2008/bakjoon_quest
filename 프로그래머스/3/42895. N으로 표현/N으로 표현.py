#N을 1개, 2개, 3개...9개 사용하는 방법
def solution(N, number): #현재 값을 가지고 나눠야 함
    answer = 0 #9개 이하로 봐야 함
    dp=[[] for _ in range(9)]#각 갯수는 1개에서부터 시작되어 2개, 3개쪽으로 하나씩 늘어남
    for i in range(1,9):
        comb_list=set()
        comb_list.add(int(str(N)*i))
        for j in range(1,i):#i번째는 1번부터 i-1번의 까지의케이스를 모두 다 한것
            for comb1 in dp[i-j]:
                for comb2 in dp[j]:
                    plus=comb1+comb2
                    minus=comb1-comb2
                    mul=comb1*comb2
                    if comb2!=0:
                        div=comb1/comb2
                        if div%1==0:
                            comb_list.add(int(div))
                    comb_list.add(plus)
                    comb_list.add(mul)
                    if minus>=0:
                        comb_list.add(minus)
        if number in comb_list:
            return i
        for q in comb_list:
            dp[i].append(q)
    
    return -1