# 다른 방법 있나,, 개느리네

def bfs(i, j, s, visited = None):   # 델타 이용해서 탐색할 거임
    '''좌표값, 지금까지 숫자의 합, visited'''
    global result
    if visited == None:             # 만약 입력받은 visited 없으면
        visited = [[0] * N for _ in range(N)] # visited 생성하고
        visited[i][j] = 1           # 시작지점에 방문 표시

    s += arr[i][j]                  # 합 추가

    if i == N - 1 and j == N - 1:   # 만약에 도착했다면
        if result > s:              # 결과 값이랑 비교해서 최소 값 갱신
            result = s
        return

    elif s > result:                  # 만약 합계가 최소값보다 높으면 중단
        return

    for k in range(2):                  # 델타 순회
        mi, mj = i + di[k], j + dj[k]   # 인덱스 안 벗어나고, 방문한 적이 없다면
        if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0:
            visited[mi][mj] = 1         # 갈 곳 방문 표시하고
            bfs(mi, mj, s, visited)     # 재귀 호출
            visited[mi][mj] = 0         # 방문 표시 취소

################################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 가로세로 칸 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0]
    dj = [0, 1]

    result = 1000001
    bfs(0, 0, 0)

    print(f'#{tc} {result}')