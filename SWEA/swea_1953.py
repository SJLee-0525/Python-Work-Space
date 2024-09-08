from collections import deque
from pprint import pprint

def bfs_2(si, sj, L):
    '''덱 사용 bfs'''
    # 초기 설정
    visited[si][sj] = 1
    Q = deque()
    Q.append((si, sj, visited[si][sj])) # 좌표와 시간 Queue에 삽입 (맨홀에 들어가는 순간 1시간임)

    while Q:
        i, j, hr = Q.popleft()  # 좌표와 시간 정보 뽑아옴
        for w in dir[tunnel[i][j]]:     # 현재 위치에서 갈 수 있는 방향 뽑아옴
            mi, mj = i + w[0], j + w[1]
            # 인덱스 벗어나지 않고, 방문한 적이 없고, 방문해도 탈출 시간 초과하지 않고, 다음 좌표가 현재 좌표와 연결 돼 있다면
            if (0 <= mi < N and 0 <= mj < M and visited[mi][mj] == 0
                    and visited[i][j] < L and list(map(lambda x: -x, w)) in dir[tunnel[mi][mj]]) : #
                # 연결됐는지 확인하려면 현재 방향 정보 전체를 뒤집은 담에 다음 위치의 방향 정보와 비교해야함:
                # list(map(lambda x: -x, w)) <<<<<<<<<< 앞에 list() 안 다니까 작동 안 하더라
                visited[mi][mj] = visited[i][j] + 1  # 방문 표시 (1시간 추가)
                Q.append((mi, mj, visited[mi][mj]))  # 좌표와 시간 정보 삽입

    # 다 돌면 방문한 곳들 카운트 후 반환
    # pprint(visited)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1
    return cnt

'''
# 재귀로 해보려 했는데, 진짜 너무 느림
# 가지를 어디서 쳐야할 지도 모르곘어..
# def dfs(si, sj, hr, L):
#     visited[si][sj] = 1 # 시작하면 전역변수 visited에 방문 표시
# 
#     if hr == L:         # 만약 레벨 끝까지 도달하면 방문할 수 있는 곳들의 개수 세서 
#         global max_cnt
#         cnt = 0
#         for i in range(N):
#             for j in range(M):
#                 if visited[i][j]:
#                     cnt += 1
#         if max_cnt < cnt: # 최대값 비교 후 갱신 및 반환
#             max_cnt = cnt
#         return
# 
#     for w in dir[tunnel[si][sj]]:       # 현재 있는 터널에서 갈 수 있는 목록 불러옴
#         mi, mj = si + w[0], sj + w[1]   # 델타
#         if 0 <= mi < N and 0 <= mj < M and list(map(lambda x:-x, w)) in dir[tunnel[mi][mj]] and visited[si][sj] >= visited[mi][mj]:
#         # 인덱스 벗어나지 않고, 건너가려는 곳과 이곳이 연결돼 있고, 재방문 하는 곳이 아니라면
#             dfs(mi, mj, hr + 1, L) # 재귀 호출
'''

############################################################################################

dir = {
    0: [[]],
    1: [[1, 0], [0, 1], [-1, 0], [0, -1]],
    2: [[1, 0], [-1, 0]],
    3: [[0, -1], [0, 1]],
    4: [[-1, 0], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[1, 0], [0, -1]],
    7: [[-1, 0], [0, -1]]
}

############################################################################################

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split()) # 배열 크기 N M / 맨홀 좌표 R C / 시간 L
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # max_cnt = 0
    # dfs(R, C, 1, L)

    print(f'#{tc} {bfs_2(R, C, L)}')
