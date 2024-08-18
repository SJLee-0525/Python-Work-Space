def find_max_summit(N):
    max_summit = 0
    for i in range(N):
        for j in range(N):
            if max_summit < mountain[i][j]:
                max_summit = mountain[i][j]
    return max_summit

def start(max_summit, N, K):
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_summit:
                dfs(i, j, K)

def dfs(i, j, K, is_cut = False, s = 0, visited = None):
    '''dfs(출발 좌표, 깎을 수 있는 크기, cut 여부, 시작 len, visited'''
    global longest

    if visited == None: # 만약 입력된 visited가 없으면 생성
        visited = [[0] * N for _ in range(N)]

    if longest < s + 1: # 경로 길이가 최대값을 갱신할 때마다 갱신
        longest = s + 1

    visited[i][j] = 1   # 방문 표시

    for l in range(4):
        mi, mj = i + di[l], j + dj[l]
        if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0:    # 만약 방문한 적이 없다면
            if mountain[mi][mj] < mountain[i][j]:      # + 방문할 곳의 높이가 현재 높이보다 낮다면
                dfs(mi, mj, K, is_cut, s + 1, visited)    # 방문할 위치에서 dfs 재호출, cut 그대로, s는 1 더하고, 갖고 있는 visited 넘겨줌

            elif is_cut == False and mountain[mi][mj] < mountain[i][j] + K:   # 만약 방문할 곳의 높이가 현재 위치보다 높지만, 깎을 수 있다면
                original_height = mountain[mi][mj]      # 일단 변경 전 높이를 임시 할당하고
                mountain[mi][mj] = mountain[i][j] - 1   # 높이 변경(내 위치보다 1 낮게)
                dfs(mi, mj, K, True, s + 1, visited)    # 방문할 위치에서 dfs 재호출, 다만 깎았으니 cut을 True로 바꿔서 호출
                mountain[mi][mj] = original_height          # 호출 했으니 원래 높이로 원상 복귀

    visited[i][j] = 0   # 다 돌고나면 다시 방문할 수 있도록 현재 위치를 not visited로 변경 (백트래킹)

##########################################################################################

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 한 변 길이, 공사 가능 깊이
    mountain = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    longest = 0
    max_summit = find_max_summit(N)
    start(max_summit, N, K)
    print(f'#{tc} {longest}')