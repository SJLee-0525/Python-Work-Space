import sys
from collections import deque

def bfs():
    queue = deque([1])

    visited = [100000001] * 101
    visited[1] = 1

    while queue:
        now = queue.popleft()

        for i in range(1, 7):
            temp = now + i
            if temp > 100:
                continue

            if visited[temp] > visited[now] + 1:
                visited[temp] = visited[now] + 1
                if adjInfo[temp] and visited[adjInfo[temp]] > visited[now] + 1:
                    visited[adjInfo[temp]] = visited[now] + 1
                    queue.append(adjInfo[temp])
                elif not adjInfo[temp]:
                    queue.append(temp)

    # print(visited)
    print(visited[100] - 1)

###################################################################

N, M = map(int, sys.stdin.readline().split())

adjInfo = [0] * 101
for _ in range(N):  # 사다리
    x, y = map(int, sys.stdin.readline().split())
    adjInfo[x] = y

for _ in range(M):  # 뱀
    x, y = map(int, sys.stdin.readline().split())
    adjInfo[x] = y

bfs()

