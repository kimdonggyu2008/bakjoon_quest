def solution(scores):
    answer=1
    minimum=scores[0]
    me=sum(scores[0])    
    scores.sort(key=lambda x:(-x[0], x[1]))
    #print(scores)
    threshold=0
    for score in scores:
        if minimum[0]<score[0] and minimum[1]<score[1]:
            return -1
        if threshold<=score[1]:
            if me<score[0]+score[1]:
                answer+=1
            threshold=score[1]
    return answer
#     for i in range(len(scores)-1): #O(n)
#         if scores[i][0]<scores[i+1][0] and scores[i][1]<scores[i+1][1]:
#             if i==0:
#                 return -1
#             scores.remove(list(scores[i][0],scores[i][1]))
#             minimum=scores[i]
#         else:
#             sums.append(sum(scores[i]))

#     if scores[len(scores)-1][0]<scores[len(scores)-2][0] and scores[len(scores)-1][1]<scores[len(scores)-2][1]:
#         scores.remove(scores[len(scores)-1])
#     else:
#         sums.append(sum(scores[len(scores)-1]))
#     sums.sort()
#     sums.reverse()
#     sukcha=1
#     for i in range(len(sums)):
#         if sums[i]>me:
#             sukcha+=1
#         else:
#             break
#     answer = sukcha
    #return answer