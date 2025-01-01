import sys
from collections import deque

def perm(lv, num):
    '''순열로 배치 가능한 궁수의 위치 찾기'''
    if lv == 3:
        game() # 궁수 위치가 정해지면 해당 배치로 게임 실행
        return

    for n in range(num, M):
        if used[n]:
            continue
        path.append(n)
        used[n] = True
        perm(lv + 1, n + 1)
        path.pop()
        used[n] = False

def game():
    '''본 게임'''
    global result, board

    board = [b[:] for b in initBoard]   # 매 게임마다 초기 보드 값으로 초기화
    killEnemy = 0
    isEnd = False                       # 게임 끝남 여부

    while not isEnd:
        targets = set()
        for archer in path:             # 각 궁수마다
            target = findTarget(archer) # bfs 탐색을 통해서 가까운 적 찾기
            if target:                  # 타겟이 있으면
                targets.add(target)     # 타겟 셋에 추가

        if targets:                     # 타겟 셋에 제거할 수 있는 적이 있으면
            for ti, tj in targets:
                board[ti][tj] = 0       # 제거
                killEnemy += 1          # 카운트 증가

        isEnd = moveEnemy()             # 적 이동과 동시에 게임 끝남 여부 재판단

    result = max(result, killEnemy)     # 게임이 끝나면 최대 값 갱신

def findTarget(archer):
    '''bfs로 타겟 찾음'''
    checked = [[0] * M for _ in range(N + 1)]
    checked[N][archer] = 1              # 궁수 자신의 위치

    queue = deque([(N, archer)])
    target = []                         # 공격 가능한 적 좌표 담을 배열

    while queue:
        i, j = queue.popleft()
        if checked[i][j] > D:           # 만약 최대 사거리 밖을 탐색하려 한다면 건너뜀
            continue

        for k in range(3):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi and 0 <= mj < M and not checked[mi][mj]:
                checked[mi][mj] = checked[i][j] + 1             # 방문 표시
                queue.append((mi, mj))
                if board[mi][mj]:                               # 만약 적이 있다면 공격 가능한 적 배열에 추가
                    target.append((checked[mi][mj], mj, mi))    # 정렬 시 가까우면서, 거리가 같을 경우 왼쪽의 적이 올 수 있게끔 추가

    if target:          # 공격 가능한 적이 있다면
        target.sort()   # 정렬
        return (target[0][2], target[0][1]) # 좌우 뒤집었던 걸 고려해서 반환
    else:
        return False

def moveEnemy():
    '''적 이동'''
    enemies = []
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                enemies.append((i, j)) # 적이 있으면 적 좌표 배열에 담고
                board[i][j] = 0        # 비움

    if not enemies: # 만약 적 배열이 비어있다면: 게임이 끝남
        return True # True 반환해서 반복 중단할 수 있도록

    for ei, ej in enemies:  # 적 배열을 순회하며
        if ei + 1 == N:     # 성에 도달한 적이 있다면 게임에서 제외
            continue
        else:               # 아니면 좌표 이동
            board[ei + 1][ej] = 1

    return False

###########################################################################

N, M, D = map(int, sys.stdin.readline().split())

initBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] + [[0] * M]
board = [b[:] for b in initBoard] # 복제

di = [0, -1, 0]
dj = [-1, 0, 1]

result = -1

used, path = [False] * M, []
perm(0, 0)  # 순열

print(result)