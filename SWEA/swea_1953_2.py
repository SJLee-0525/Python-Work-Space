from collections import deque

def bfs(si, sj, L):
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    Q = deque()
    Q.append((si, sj, visited[si][sj]))  # 좌표와 시간 Queue에 삽입 (맨홀에 들어가는 순간 1시간임)
    cnt = 1 # 갈 수 있는 곳 개수

    while Q:
        i, j, hr = Q.popleft()       # 좌표와 시간 정보 뽑아옴
        for w in dir[tunnel[i][j]]:  # 현재 위치에서 갈 수 있는 방향 뽑아옴
            mi, mj = i + w[0], j + w[1]
            # 인덱스 벗어나지 않고, 방문한 적이 없고, 터널이 있으며,
            # 방문해도 탈출 시간 초과하지 않고, 다음 좌표가 현재 좌표와 연결 돼 있다면
            if (0 <= mi < N and 0 <= mj < M and visited[mi][mj] == 0 and tunnel[mi][mj]
                    and hr < L and list(map(lambda x:-x, w)) in dir[tunnel[mi][mj]]):
                # 연결됐는지 확인할 때 현재 방향 정보 전체를 뒤집은 담에 다음 위치의 방향 정보와 비교해봤음.
                # list(map(lambda x:-x, w)) <<<<<<<<<< 앞에 list() 안 다니까 작동 안 하더라
                cnt += 1                             # 갈 수 있는 곳 개수 추가 하고
                visited[mi][mj] = hr + 1             # 방문 표시에 시간 정보 추가 (1시간 추가)
                Q.append((mi, mj, visited[mi][mj]))  # 좌표와 시간 정보 삽입

    return cnt

############################################################################################

dir = {
    1: [[1, 0], [0, 1], [-1, 0], [0, -1]],
    2: [[1, 0], [-1, 0]],
    3: [[0, -1], [0, 1]],
    4: [[-1, 0], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[1, 0], [0, -1]],
    7: [[-1, 0], [0, -1]]
}

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())  # 배열 크기 N M / 맨홀 좌표 R C / 시간 L
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {bfs(R, C, L)}')