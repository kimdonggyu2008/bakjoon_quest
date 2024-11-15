import heapq
def solution(genres, plays):#각 장르별 총합 딕셔너리,값 저장용 딕셔너리 
    answer = []
    summed={}
    datas={}
    
    for i,(genre, play) in enumerate(zip(genres,plays)):
        if genre not in summed:
            summed[genre]=play
            datas[genre]=[(play,i)]
        else:
            summed[genre]+=play
            datas[genre].append((play,i))
    sorted_genres=sorted(summed.keys(),key=lambda x:summed[x],reverse=True) #키값 기준으로 정렬
    
    for genre in sorted_genres:
        top_songs=sorted(datas[genre], key=lambda x: (-x[0],x[1]))[:2]
        for play, idx in top_songs:
            answer.append(idx)
    return answer
        