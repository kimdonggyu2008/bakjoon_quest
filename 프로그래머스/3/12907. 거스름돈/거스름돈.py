# def DP(now,money,left,memo):
#     if left==0:#마지막인 경우, 경우의 수는 1개임
#         return 1
#     if left<0 or now==len(money):# 끝까지 다 도달한 경우
#         return 0
#     if (now,left) in memo: #이전의 계산값 존재할 시
#         return memo[(now,left)]
#     result= DP(now+1,money,left,memo)+DP(now,money,left-money[now],memo)#현재 화폐를 안 사용, 사용하는 경우
#     memo[(now,left)]=result
#     return result
        
# def solution(n, money):
#     answer = 0
#     # 각 화폐를 아랫단계 화폐로 만드는 방법을 찾고
#     # 가장 큰 화폐 갯수로 나눈 후, 방법을 곱하면 되지 않을까?
#     memo={}
#     answer=DP(0,money,n,memo)
#     return answer% 1000000007

def solution(n,money):
    dp=[1]+[0]*n
    for coin in money:
        for price in range(coin,n+1):
            if price >=coin:
                dp[price]+=dp[price-coin]
    return dp[n]% 1000000007