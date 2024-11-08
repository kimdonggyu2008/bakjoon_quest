# def solution(commands):
#     answer = []
#     merged = []  # 병합된 인덱스들을 저장할 리스트
#     datas = []   # 각 셀의 값을 저장할 리스트 (딕셔너리 형태로 관리)
    
#     for command in commands:
#         command = command.split()
#         now_command = command[0]
#         print("Merged:", merged)
#         print("Datas:", datas)
        
#         if now_command == "UPDATE":
#             if len(command) == 4:
#                 r = int(command[1])
#                 c = int(command[2])
#                 value = command[3]
#                 datas.append({"value": value, "r": r, "c": c})
            
#             elif len(command) == 3:
#                 value1 = command[1]
#                 value2 = command[2]
#                 for data in datas:
#                     if data["value"] == value1:
#                         data["value"] = value2
        
#         elif now_command == "MERGE":
#             r1 = int(command[1])
#             c1 = int(command[2])
#             r2 = int(command[3])
#             c2 = int(command[4])
            
#             if [r1, c1] == [r2, c2]:  # 동일한 셀
#                 continue
            
#             # 병합된 리스트에 이미 포함된지 확인
#             merged_cell_found = False
#             for merge in merged:
#                 if [r1, c1] in merge or [r2, c2] in merge:
#                     merge.append([r1, c1])
#                     merge.append([r2, c2])
#                     merged_cell_found = True
#                     break
            
#             # 기존 병합에 없으면 새롭게 병합 추가
#             if not merged_cell_found:
#                 merged.append([[r1, c1], [r2, c2]])
#             print("병합 진행 완료")
        
#         elif now_command == "UNMERGE":
#             r1 = int(command[1])
#             c1 = int(command[2])
            
#             # 해당 셀이 포함된 병합 그룹을 찾고 제거
#             for merge in merged:
#                 if [r1, c1] in merge:
#                     merge.remove([r1, c1])
#                     if len(merge) <= 1:
#                         merged.remove(merge)
#                     break
        
#         elif now_command == "PRINT":
#             r = int(command[1])
#             c = int(command[2])
            
#             # 해당 좌표에 맞는 데이터를 찾고 출력
#             cell_value = "EMPTY"
#             for data in datas:
#                 if data["r"] == r and data["c"] == c:
#                     cell_value = data["value"]
#                     break
#             print(cell_value)
#             answer.append(cell_value)
    
#     return answer

parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [["EMPTY"] * 51 for _ in range(51)]
result = []

# 최상위 부모 좌표를 찾는 함수
def find(r, c):
    if (r, c) == parent[r][c]:
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

# 두 좌표를 병합하는 함수
def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]

# 특정 좌표 (r, c)에 값을 업데이트하는 함수
def UPDATE(r, c, msg):
    pr, pc = find(r, c)
    cells[pr][pc] = msg

# 특정 값 msg1을 msg2로 업데이트하는 함수
def UPDATE_VAL(msg1, msg2):
    for r in range(51):
        for c in range(51):
            pr, pc = find(r, c)
            if cells[pr][pc] == msg1:
                cells[pr][pc] = msg2

# 두 좌표를 병합하는 함수
def MERGE(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    
    if (r1, c1) == (r2, c2):
        return
    if cells[r1][c1] != "EMPTY":
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)

# 특정 좌표의 병합을 해제하는 함수
def UNMERGE(r, c):
    pr, pc = find(r, c)
    msg = cells[pr][pc]
    
    # 병합된 모든 좌표 리스트 추출
    merge_list = []
    for ar in range(51):
        for ac in range(51):
            apr, apc = find(ar, ac)
            if (apr, apc) == (pr, pc):
                merge_list.append((ar, ac))
    
    # 병합 해제 후 원래 위치에 메시지 남기고 나머지는 비움
    for ar, ac in merge_list:
        parent[ar][ac] = (ar, ac)
        cells[ar][ac] = "EMPTY" if (ar, ac) != (r, c) else msg

# 특정 좌표의 값을 출력하는 함수
def PRINT(r, c):
    pr, pc = find(r, c)
    result.append(cells[pr][pc])

# 명령어를 처리하는 solution 함수
def solution(commands):
    for command in commands:
        cmd, *arg = command.split()
        if cmd == "UPDATE":
            if len(arg) == 3:  # UPDATE r c value 형태
                r, c, value = arg
                UPDATE(int(r), int(c), value)
            else:  # UPDATE value1 value2 형태
                value1, value2 = arg
                UPDATE_VAL(value1, value2)
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, arg)
            MERGE(r1, c1, r2, c2)
        elif cmd == "UNMERGE":
            r, c = map(int, arg)
            UNMERGE(r, c)
        elif cmd == "PRINT":
            r, c = map(int, arg)
            PRINT(r, c)
    
    return result
