import sys
from collections import deque

def bfs(si, sj, N, visited):
    visited[si][sj] = 1     # 시작 지점에 방문 표시
    Q = deque()             # bfs 순회용 Queue
    Q.append((si, sj))      # Queue에 현재 좌표 추가
    temp = []               # 방문 기록을 남길 리스트
    temp.append((si, sj))   # 방문 기록 남길 리스트에도 좌표 추가
    pop_sum = arr[si][sj]   # 방문한 곳의 인구수 합계를 담을 변수
    nat_cnt = 1             # 방문한 나라 수를 세는 변수
    while Q:
        i, j = Q.popleft()  # Q에서 좌표 받아와서
        for k in range(4):  # 델타 탐색
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0 and L <= abs(arr[i][j] - arr[mi][mj]) <= R:
            # index를 벗어나지 않고, 방문한 적이 없으며, 두 나라 인구수의 차가 L 이상 R 이하이면
                visited[mi][mj] = 1      # 방문
                Q.append((mi, mj))       # Queue에 좌표 추가
                temp.append((mi, mj))    # 방문 기록에도 추가
                pop_sum += arr[mi][mj]   # 인구수 합계 추가
                nat_cnt += 1             # 나라 카운트 추가

    # bfs 순회가 끝나면
    res_pop = pop_sum // nat_cnt # 이동한 인구 수 계산
    for i2, j2 in temp:          # 방문 기록 리스트에 있는 좌표들의 인구를
        arr[i2][j2] = res_pop    # 이동한 인구 수로 재할당

#################################################################################################

N, L, R = map(int, sys.stdin.readline().split())                    # 배열 크기, L 이상, R 이하
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 나라의 인구수 배열

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

day = 0
while 1:
    visited = [[0] * N for _ in range(N)]   # 반복마다 visited 새로 생성
    cnt = 0                                 # 인구 이동이 있었는지 확인하는 변수
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:          # 방문한 적이 없는 곳이라면
                cnt += 1                    # 인구 이동 확인 변수 늘리고
                bfs(i, j, N, visited)       # bfs 탐색

    if cnt == N ** 2: # 만약 인구 이동 확인 변수가 N ** 2라면 : bfs가 배열 모든 곳에서 돌았다는 뜻 (각 나라별 국경이 전부 닫혀있음)
        break         # 중단

    day += 1          # 날짜 카운트 증가

print(day)