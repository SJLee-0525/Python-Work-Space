from collections import deque

def bfs():
    Q = deque()

    # 큐에 주변에 L을 가진 W의 좌표를 저장
    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'W':
                for k in range(4):
                    mi, mj = i + di[k], j + dj[k]
                    # 만약 주변이 전부 W라면 그거보다 육지에 가까운 W가 존재하기에 담을 필요 없을듯
                    if 0 <= mi < N and 0 <= mj < M and beach[mi][mj] == 'L':
                        Q.append((i, j))
                        distance[i][j] = 1  # 거리 표시도 지금 미리 해둠 (마지막에 -1 해줘야함)
                        break

    # BFS
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < M and distance[mi][mj] == 0:
                Q.append((mi, mj))
                distance[mi][mj] = distance[i][j] + 1


def cal_distance(N, M):
    s = 0
    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'L':
                s += distance[i][j] - 1 # distance에 저장된 값보다 1 적게 계산해야 함
    return s

#####################################################################################

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())    # N 세로, M 가로
    beach = [list(input()) for _ in range(N)]
    distance = [[0] * M for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    bfs()

    print(f'#{tc} {cal_distance(N, M)}')
