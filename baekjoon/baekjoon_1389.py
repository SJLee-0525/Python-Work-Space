import sys
from collections import deque

def bfs(per, target, N):
    visited = [0] * (N + 1)
    Q = deque()
    visited[per] = 1
    Q.append(per)
    while Q:
        p = Q.popleft()
        for w in adjL[p]:
            if visited[w] == 0:
                visited[w] = visited[p] + 1
                if w == target:
                    return visited[w] - 1
                Q.append(w)
    return 0

N, M = map(int, sys.stdin.readline().split())
# 유저 수 / 관계 수
adjL = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

# print(adjL)

temp = []
for per in range(1, N + 1): # 모든 사람을 한 번씩 기준으로 삼아서
    temp_sum = 0
    for target in range(1, N + 1):  # 자신을 제외한 사람을 타겟으로 한 번씩 bfs 돌리고
        if target != per:
            temp_sum += bfs(per, target, N) # 합을 추가
    temp.append(temp_sum)

print(temp.index(min(temp)) + 1) # 리스트에서 값이 가장 낮은 인덱스를 반환