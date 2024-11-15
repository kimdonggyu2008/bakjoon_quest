

# from collections import deque

# def greedy(i,rotate,used,result):
#     if i>=len(rotate):
#         return result
#     if True not in used:#쓸 수 있는게 없는 경우
#         return result
    
    
#     if used[i]:#현재 위치를 쓸 수 있는 경우
#         used_copy=used[:]
#         if i==0:#첫번째
#             used_copy[-1]=False
#             used_copy[i]=False
#             used_copy[i+1]=False
#         elif i==len(used)-1:#마지막
#             used_copy[i-1]=False
#             used_copy[i]=False
#             used_copy[0]=False
#         else:
#         #if 0<i<len(used):#중간
#             used_copy[i-1]=False
#             used_copy[i]=False
#             used_copy[i+1]=False
#         pick=greedy(i+1,rotate,used_copy,result+rotate[i]) #넣은 경우, used를 바꾸고, 값 업데이트
#     else:
#         pick=result #안 넣은 경우에는 그대로 가져가야 함 
#     skip=greedy(i+1,rotate,used,result) #안 넣고 다음으로 넘어가는 경우
#     return max(pick,skip)
    
# def solution(sticker):
#     used=[True for _ in range(len(sticker))]
#     answer=greedy(0,sticker,used,0)

#     return answer          # list를 반환

def solution(sticker):
    if len(sticker)==1:
        return sticker[0]
    
    d1,d2=[0]*len(sticker),[0]*len(sticker)
    
    d1[0]=sticker[0]#첫번째 값
    d1[1]=d1[0]
    for i in range(2,len(sticker)-1):#첫번째 뜯은 경우
        d1[i]=max(d1[i-2]+sticker[i],d1[i-1])
            
    for i in range(1,len(sticker)):#첫번째 안 뜯은 경우
        d2[i]=max(d2[i-2]+sticker[i],d2[i-1])
    return max(d1[-2],d2[-1])
