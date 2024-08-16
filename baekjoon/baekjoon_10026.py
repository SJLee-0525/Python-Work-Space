# 함수 내에서 색 구분을 할 수 있게 두면 배열을 deepcopy하지 않아도 되고, 함수 갯수를 줄일 수 있을 것 같음
# 하지만 나는 못했지

import sys
import copy
from collections import deque

# 색맹이 아닌 사람 기준으로 출발점 찾기
def find_start(N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if pic[i][j] != 0:          # 색이 있다면,
                DFS(i, j, N, pic[i][j]) # 해당 좌표와 색 정보를 함께 전달
                cnt += 1
    return cnt

# 색맹인 사람 기준으로 출발점 찾기
def find_start_blindness(N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if blindness_pic[i][j] != 0:
                DFS_blindness(i, j, N, blindness_pic[i][j])
                cnt += 1
    return cnt

# 좌표와 색 정보를 전달받음
def DFS(si, sj, N, color):
    visited = [[0] * N for _ in range(N)]
    stack = []

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    visited[si][sj] = 1
    pic[si][sj] = 0
    i, j = si, sj
    while 1:
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]   # 자기와 같은 색인 경우 탐색
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0 and pic[mi][mj] == color:
                stack.append((i, j))
                i, j = mi, mj
                visited[i][j] = 1
                pic[i][j] = 0   # 색 탐색 후에는 중복 탐색 없도록 값을 바꿔놓음
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                return

def DFS_blindness(si, sj, N, color):
    visited = [[0] * N for _ in range(N)]
    stack = []

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    visited[si][sj] = 1
    blindness_pic[si][sj] = 0
    i, j = si, sj
    while 1:
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0 and blindness_pic[mi][mj] == color:
                stack.append((i, j))
                i, j = mi, mj
                visited[i][j] = 1
                blindness_pic[i][j] = 0
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                return
#############################################################

N = int(sys.stdin.readline())

pic = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# 색맹인 사람이 보는 것처럼 빨간색을 G로 바꿔놓음
blindness_pic = copy.deepcopy(pic)
for i in range(N):
    for j in range(N):
        if blindness_pic[i][j] == "R":
            blindness_pic[i][j] = "G"

print(find_start(N), end=' ')
print(find_start_blindness(N))