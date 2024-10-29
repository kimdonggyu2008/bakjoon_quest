# from itertools import combinations

# def has_sum(cards, target):
#     return any(sum(pair) == target for pair in combinations(cards, 2))


# def DP(coin,cards,mine,n,result):
#     if n==len(cards)-1:
#         return result
#     else:
#         if coin>=2 and has_sum(mine,n+1):
#             mine+=cards[n:n+1]
#             result=max(DP(coin,cards,mine,n+2, result+1),result)
#         elif coin>=1 and has_sum(mine,n+1,result+1):
#             temp1=mine+cards[n]
#             temp2=mine+cards[n+1]
#             a=DP(coin-1,cards,temp1,n+2,result+1)
#             b=DP(coin-1,cards,temp2,n+2,result+1)
#             result=max(a,b,result)
#         elif coin==0 and has_sum(mine,n+1):
#             result=max(DP(coin,cards,mine,n+2, result+1),result   )
#     return result


# def solution(coin, cards):
#     answer=play_game(coin,cards)
#     return answer

from collections import deque

def check(mine,cards,target):#해당 n+1을 맞추는 값이 있는지 확인
    operand=set(cards)
    for card in mine:
        if target-card in operand:
            mine.remove(card)
            cards.remove(target-card)
            return True
    return False

def solution(coin, cards):
    n=len(cards)
    mine=cards[:n//3]
    yours=deque(cards[n//3:])
    pending=[]
    turn=1
    while coin>=0 and yours: #
        pending.append(yours.popleft())
        pending.append(yours.popleft())
        if check(mine,mine,n+1):
            pass
        elif coin>=1 and check(mine,pending,n+1):
            coin-=1
        elif coin>=2 and check(pending,pending,n+1):
            coin-=2
        else:
            break
        turn+=1
    return turn


