import sys
from collections import deque

def fireStorm(L):
    rotating(L)
    melting()

def rotating(L):
    '''90도 회전'''
    # zip 사용해서 90도 회전하기 ( Python3 : { 메모리: 35084 KB, 시간: 4408 ms }, PyPy3: { 메모리: 117748 KB, 시간: 876 ms } )
    # for si in range(0, 2 ** N, L):
    #     for sj in range(0, 2 ** N, L):
    #         sub_grid = [row[sj:sj + L] for row in board[si:si + L]]
    #
    #         rotated = list(zip(*sub_grid[::-1]))
    #
    #         for i in range(L):
    #             board[si + i][sj:sj + L] = rotated[i]

    # # 막무가내로 90도 회전하기 ( Python3: { 메모리: 35092 KB, 시간: 4352 ms }, PyPy3: { 메모리: 116736 KB, 시간: 608 ms } )
    store = deque([])

    for si in range(0, 2 ** N, L):
        for sj in range(0, 2 ** N, L):

            for i in range(si, si + L):
                for j in range(sj, sj + L):
                    store.append(board[i][j])

            for j2 in range(sj + L - 1, sj - 1, -1):
                for i2 in range(si, si + L):
                    board[i2][j2] = store.popleft()

def melting():
    '''board 전체를 순회하며 녹여야 하는지 판별 후 녹이는 함수'''
    store = []  # 녹여야 하는 좌표 저장하는 배열

    for i in range(2 ** N):
        for j in range(2 ** N):
            if board[i][j]: # 해당 좌표에 얼음이 있다면
                adjCnt = 0  # 카운트 할당
                for k in range(4):  # 델타 순회
                    mi, mj = i + di[k], j + dj[k]
                    if 0 <= mi < 2 ** N and 0 <= mj < 2 ** N and board[mi][mj]:
                        adjCnt += 1 # 인접한 곳에 얼음이 있다면 카운트

                if adjCnt < 3:      # 인접한 얼음이 3개 미만이라면 좌표 저장
                    store.append((i, j))

    for i, j in store:  # 저장된 좌표 뽑아서 녹임
        board[i][j] -= 1

def check():
    '''모든 파이어스톰 시전 후 얼음 점검'''
    for i in range(2 ** N):
        for j in range(2 ** N):
            if board[i][j] and not checked[i][j]: # 얼음이 존재하고 방문한 적이 없다면
                bfs(i, j)                         # 해당 좌표로 bfs 탐색

def bfs(si, sj):
    global totalIce, maxIceSize

    queue = deque([(si, sj)])   # 큐 생성 및 시작 좌표 삽입
    checked[si][sj] = True      # 방문 표시

    iceSize = 1                 # 해당되는 얼음의 bfs 탐색에서 해당되는 얼음의 크기 측정
    while queue:
        i, j = queue.popleft()
        totalIce += board[i][j] # 전체 얼음의 양 연산

        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            # 인접한 곳이 얼음이고, 방문한 적이 없다면
            if 0 <= mi < 2 ** N and 0 <= mj < 2 ** N and board[mi][mj] and not checked[mi][mj]:
                queue.append((mi, mj))  # 큐 삽입
                checked[mi][mj] = True  # 방문 표시
                iceSize += 1            # 얼음 크기 증가

    maxIceSize = max(maxIceSize, iceSize)   # 해당 bfs 탐색이 끝난 후 가장 큰 덩어리 값 재연산

################################################################################

N, Q = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N)]
fireStorms = tuple(map(int, sys.stdin.readline().split()))

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

for level in fireStorms:
    fireStorm(2 ** level)

totalIce = 0
maxIceSize = 0
checked = [[False] * (2 ** N) for _ in range(2 ** N)]

check()

print(totalIce)
print(maxIceSize)