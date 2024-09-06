def find_summit():
    temp = 0
    temp_list = []
    for i in range(N):
        for j in range(N):
            if temp < mountain[i][j]:
                temp = mountain[i][j]
                temp_list = [(i, j)]
            elif temp == mountain[i][j]:
                temp_list.append((i, j))
    return temp, temp_list

def cnst(i, j, i_mountain, visited=None, caved=False):
    global rst

    if visited == None:
        visited = [[0] * N for _ in range(N)]
        visited[i][j] = 1

    if rst < visited[i][j]:
        rst = visited[i][j]

    for k in range(4):
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0 and i_mountain[mi][mj] < mountain[i][j]:
            visited[mi][mj] = visited[i][j] + 1
            cnst(mi, mj, i_mountain, visited, caved)
            visited[mi][mj] = 0

        elif caved == False and 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0 and i_mountain[mi][mj] - K < mountain[i][j]:
            temp_height = i_mountain[mi][mj]
            i_mountain[mi][mj] = i_mountain[i][j] - 1
            visited[mi][mj] = visited[i][j] + 1
            caved = True
            cnst(mi, mj, i_mountain, visited, caved)
            i_mountain[mi][mj] = temp_height
            visited[mi][mj] = 0
            caved = False

    return

###################################################################

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

###################################################################

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split()) # 한 변의 길이, 공사 가능 깊이
    mountain = [list(map(int, input().split())) for _ in range(N)]

    rst = 0
    summit, summit_list = find_summit()

    for si, sj in summit_list:
        cnst(si, sj, mountain)

    print(f'#{tc} {rst}')


