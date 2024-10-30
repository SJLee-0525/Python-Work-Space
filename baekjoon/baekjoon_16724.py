import sys
import pprint

dirDict = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def find(i, j):
    di, dj = dirDict[arr[i][j]]
    mi, mj = i + di, j + dj
    if 0 <= mi < N and 0 <= mj < M:
        pass

def dfs(i, j, c):
    visited[i][j] = c
    if Fvisited[i][j] > c:
        Fvisited[i][j] = c

    di, dj = dirDict[arr[i][j]]
    mi, mj = i + di, j + dj
    if 0 <= mi < N and 0 <= mj < M and not visited[mi][mj]:
        dfs(mi, mj, c)


N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# print(arr)

min_result = set()
Fvisited = [[100000] * M for _ in range(N)]
c = 1
for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        dfs(i, j, c)
        c += 1

pprint.pprint(Fvisited)

a = set()
for i in range(N):
    for j in range(M):
        a.add(Fvisited[i][j])

print(a)
print(len(a))



