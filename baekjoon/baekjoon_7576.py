import sys
from collections import deque

def bfs():
    global max_progress
    Q = deque()

    # 초기 Queue 생성: 익어있는 토마토가 있으면, 큐에 넣고, progress 표시하고, 토마토가 없으면 progress에 표시
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                Q.append((i, j))
                progress[i][j] = 1
            elif box[i][j] == -1:
                progress[i][j] = -1

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < M and box[mi][mj] == 0 and progress[mi][mj] == 0:
                Q.append((mi, mj))
                progress[mi][mj] = progress[i][j] + 1
                if max_progress < progress[i][j] + 1: # 최대 날짜 할당
                    max_progress = progress[i][j] + 1

def init_check():
    '''초기 상태 검사'''
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True # 만약 모든 토마토가 비어있거나 익어있으면, 굳이 돌릴 필요 없음

def check():
    '''탐색 끝난 뒤 검사'''
    for i in range(N):
        for j in range(M):
            if progress[i][j] == 0:
                return False # 만약 다 했는데 안 익은 토마토가 있으면 false 반환
    return True

#################################################################################

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

progress = [[0] * M for _ in range(N)]
max_progress = 0

if not init_check(): # 만약 안 익은 토마토가 있으면
    bfs()            # bfs 탐색 후
    if check():      # 안 익은 토마토 없으면
        print(max_progress - 1) # 날짜 출력
    else:            # 안 익은 토마토 있으면
        print(-1)    # -1 출력
else:                # 초기에 더 이상 익을 토마토가 없으면
    print(0)         # 0 출력

