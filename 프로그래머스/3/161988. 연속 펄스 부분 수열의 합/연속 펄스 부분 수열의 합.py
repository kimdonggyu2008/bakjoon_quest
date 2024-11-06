from sys import maxsize

INF=maxsize

def check(sequence):
    #결과는 처음부터 1,-1을 계속 곱하거나, 0부터 시작해서 다 더하는 경우
    result= -INF
    pulse=1
    s1=s2=0
    s1_min=s2_min=0
    
    for i in range(len(sequence)):
        s1+=sequence[i]*pulse
        s2+=sequence[i]*(-pulse)
        
        result=max(result,s1-s1_min,s2-s2_min)
        
        s1_min=min(s1_min,s1)
        s2_min=min(s2_min,s2)
        
        pulse*=-1
        # if add==True:
        # #sequence[i], 이전값+sequence[i]*-1, 이전값+sequence[i]*1
        #     result=max(sequence[i],result+sequence[i]*-1,0)
        #     add=False
        # else:
        #     result=max(sequence[i],result+sequence[i]*1,0)
        #     add=True
    return result
            
                

def solution(sequence):
    return check(sequence)
    #return answer