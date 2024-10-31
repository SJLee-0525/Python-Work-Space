import sys
sys.setrecursionlimit(1000001)

dirDict = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

# 델타 순회용
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 재귀 (recursion 걸리긴 하나 조금 더 빠름)
def dfs(i, j, c):
    visited[i][j] = c   # 방문 표시

    for k in range(4):  # 델타 순회
        mi, mj = i + di[k], j + dj[k]
        if (0 <= mi < N and 0 <= mj < M and visited[mi][mj] < c
            and dirDict[arr[mi][mj]][0] == -di[k] and dirDict[arr[mi][mj]][1] == -dj[k]):
        # 범위를 벗어나지 않고, 방문한 적이 없거나 방문한 적이 있더라도 덮어씌울 수 있다면 (후순위 탐색에서 추가 방문)
        # 또 다음 위치에서 현재 위치로 올 수 있다면 (방향이 연결되어 있다면)
            dfs(mi, mj, c) # 다음 탐색

# # stack 간당간당하게 통과
# def dfs(si, sj, c):
#     stack = []
#     i, j = si, sj
#     visited[i][j] = c
#
#     while 1:
#         for k in range(4): # 델타 순회
#             mi, mj = i + di[k], j + dj[k]
#             if (0 <= mi < N and 0 <= mj < M and visited[mi][mj] < c
#                 and dirDict[arr[mi][mj]][0] == -di[k] and dirDict[arr[mi][mj]][1] == -dj[k]):
#             # 범위를 벗어나지 않고, 방문한 적이 없거나 방문한 적이 있더라도 덮어씌울 수 있다면 (후순위 탐색에서 추가 방문)
#             # 또 다음 위치에서 현재 위치로 올 수 있다면 (방향이 연결되어 있다면)
#                 stack.append((i, j)) # 스택에 푸시
#                 i, j = mi, mj        # 이동
#                 visited[i][j] = c    # 방문 표시
#                 break                # 다음 위치에서 델타 순회
#         else:
#             if stack:                # 해당 위치에서 더 갈 수 있는 곳이 없다면
#                 i, j = stack.pop()   # 스택에서 이전 방문 좌표 뽑아와서 다시 델타 순회
#             else:                    # 없으면 중단
#                 return

####################################################################

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited, cnt = [[0] * M for _ in range(N)], 1

for i in range(N):
    for j in range(M):
        if visited[i][j]: # 만약 이미 전에 방문됐다면 : 어떤 좌표의 사이클이었을 것
            continue      # -> 스킵
        dfs(i, j, cnt)    # 아니면 dfs 탐색 후
        cnt += 1          # visited에 할당할 값 변경

a = set()  # 중복 제거용
for i in range(N):
    for j in range(M):
        a.add(visited[i][j]) # visited에 있는 cnt 값들 set에 추가

print(len(a))   # set 길이 출력