# def solution(gems):
#     answer = []
#     gems_real=len(list(set(gems)))#보석 갯수
#     end=0
#     temp=[]
#     for start in range(len(gems)):#시작부분을 0부터 끝까지 이동
#         temp=[]
#         print("시작점",start)
#         while len(list(set(temp)))<gems_real and end<len(gems):#길이, 끝까지 가기 전까지
#         #while end<len(gems):#길이, 끝까지 가기 전까지
#             temp.append(gems[end])
#             end+=1
#             print("현재 문자열",temp)
#             #print(len(list(set(temp))))
#             if len(list(set(temp)))==gems_real:
#                 answer.append([start+1,end])
#         temp.remove(temp[0])
#         print()
#     return answer[0]
def solution(gems):
    gem = list(set(gems))
    n = len(gem)
    
    dic = {gems[0]: 1}
    answer = [1, len(gems)]
    left,right = 0,0
    while left <= right and right < len(gems):
        if len(dic) == n:
            if answer[1]-answer[0] > right-left:
                answer = [left+1, right+1]
            
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1

        elif len(dic) < n:
            right += 1
            if right >= len(gems):
                break
            if gems[right] not in dic:
                dic[gems[right]] = 1
            else:
                dic[gems[right]] += 1
        
    return answer