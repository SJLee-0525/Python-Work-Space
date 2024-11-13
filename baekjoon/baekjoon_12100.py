import sys

def perm(lv):
    '''
    중복 순열로 조작 가능한 모든 경우의 수 생성
    [0: 우, 1: 하, 2: 좌, 3: 상]
    '''
    if lv == 5:     # 모든 경우의 수를 만들면 해당 순서로 조작 메서드 호출
        moveBoard(0)
        return

    for d in range(4):
        sequence.append(d)
        perm(lv + 1)
        sequence.pop()

# 우 하 좌 상
def moveBoard(lv):
    '''만들어진 조작 순서대로 재귀를 통해 조작하는 함수'''
    global board, result

    if lv == 5: # 조작이 다 끝나면 최대 값 비교 후 할당
        for i in range(N):
            for j in range(N):
                result = max(result, board[i][j])
        return

    memoBoard = [b[:] for b in board]   # 추후 맵 복구를 위한 맵 복제
    valueList = []                      # 블록을 합치고 이동시킬때 사용할 배열
    if sequence[lv] == 0:               # 우측으로 쓸기: 각자 방향에 맞게끔 board 순회
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[i][j]:         # 해당 위치에 블록이 있으면 valueList에 값 추가, False는 추후 합쳤는지 확인할 용도
                    valueList.append([board[i][j], False])
                    board[i][j] = 0     # 이동할 거니까 0으로 바꿔서 맵 초기화

            if valueList:               # 만약 valueList에 값이 있다면
                temp = [valueList[0]]   # temp에 첫번째 값 할당
                if len(valueList) >= 2: # 만약 2개 이상의 값이 valueList에 있다면
                    for v in range(1, len(valueList)):  # temp의 가장 마지막 요소와 해당 valueList 값과 비교
                        # 둘이 값이 같고, 이번 턴에서 합쳐진 적이 없다면
                        if temp[-1][0] == valueList[v][0] and temp[-1][1] == valueList[v][1] == False:
                            temp[-1][0] += valueList[v][0]  # 합치고
                            temp[-1][1] = True              # 합친 것 표시
                        else:   # 만약 둘이 값이 같지 않거나 합쳐졌던 적이 있는 애가 하나라도 있다면
                            temp.append(valueList[v])   # 그냥 temp에 추가

                for t in range(len(temp)):  # temp를 순회하며 board의 적절한 위치에 값 할당
                    board[i][N - 1 - t] = temp[t][0]

            valueList.clear()  # 다음 탐색을 위해 valueList 초기화, 이하 동일

    elif sequence[lv] == 1:         # 하단으로 쓸기
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[j][i]:
                    valueList.append([board[j][i], False])
                    board[j][i] = 0

            if valueList:
                temp = [valueList[0]]
                if len(valueList) >= 2:
                    for v in range(1, len(valueList)):
                        if temp[-1][0] == valueList[v][0] and temp[-1][1] == valueList[v][1] == False:
                            temp[-1][0] += valueList[v][0]
                            temp[-1][1] = True
                        else:
                            temp.append(valueList[v])

                for t in range(len(temp)):
                    board[N - 1 - t][i] = temp[t][0]

            valueList.clear()

    elif sequence[lv] == 2:         # 좌측으로 쓸기
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    valueList.append([board[i][j], False])
                    board[i][j] = 0

            if valueList:
                temp = [valueList[0]]
                if len(valueList) >= 2:
                    for v in range(1, len(valueList)):
                        if temp[-1][0] == valueList[v][0] and temp[-1][1] == valueList[v][1] == False:
                            temp[-1][0] += valueList[v][0]
                            temp[-1][1] = True
                        else:
                            temp.append(valueList[v])

                for t in range(len(temp)):
                    board[i][t] = temp[t][0]

            valueList.clear()

    elif sequence[lv] == 3:         # 상단으로 쓸기
        for i in range(N):
            for j in range(N):
                if board[j][i]:
                    valueList.append([board[j][i], False])
                    board[j][i] = 0

            if valueList:
                temp = [valueList[0]]
                if len(valueList) >= 2:
                    for v in range(1, len(valueList)):
                        if temp[-1][0] == valueList[v][0] and temp[-1][1] == valueList[v][1] == False:
                            temp[-1][0] += valueList[v][0]
                            temp[-1][1] = True
                        else:
                            temp.append(valueList[v])

                for t in range(len(temp)):
                    board[t][i] = temp[t][0]

            valueList.clear()

    moveBoard(lv + 1)                   # 작업 수행 후에는 다음 단계 재귀 호출
    board = [mb[:] for mb in memoBoard] # 맵 복구

##############################################################################

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result, sequence = 0, []
perm(0)

print(result)