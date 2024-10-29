import sys
import heapq

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dijkstra(si, sj):
    priorityQueue = []
    heapq.heappush(priorityQueue, (0, si, sj))

    visited[si][sj] = 1
    destroy[si][sj] = 0

    while priorityQueue:
        destroyCnt, i, j = heapq.heappop(priorityQueue)
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < M and not visited[mi][mj]:
                if arr[mi][mj] and destroy[mi][mj] > destroyCnt + 1:
                    arr[mi][mj] = 0
                    visited[mi][mj] = 1
                    destroy[mi][mj] = destroyCnt + 1
                    heapq.heappush(priorityQueue, (destroyCnt + 1, mi, mj))
                elif not arr[mi][mj] and destroy[mi][mj] > destroyCnt + 1:
                    visited[mi][mj] = 1
                    destroy[mi][mj] = destroyCnt
                    heapq.heappush(priorityQueue, (destroyCnt, mi, mj))

    return destroy[ti][tj]

##########################################################################

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

si, sj, ti, tj = 0, 0, N - 1, M - 1

visited = [[0] * M for _ in range(N)]
destroy = [[100001] * M for _ in range(N)]

print(dijkstra(0, 0))
