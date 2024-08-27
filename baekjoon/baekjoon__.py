import sys

def dfs(s):
    global out_visited
    visited = [0] * (N + 1)
    visited[s] = 1
    out_visited[s] = 1
    stack = []
    while 1:
        for w in adjL[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                out_visited[s] = 1
                # if sum(out_visited) == N:
                #     return 1
                break
            else:
                return 0
        else:
            if stack:
                s = stack.pop()
            else:
                return 1
    
##########################################################################

T = 1
while 1:
    T += 1
    N, M = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 수
    if N == 0 and M == 0:
        break

    adjL = [[] for _ in range(N + 1)]
    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        adjL[v1].append(v2)
        # adjL[v2].append(v1)

    print(adjL)
    rst = 0
    out_visited = [0] * (N + 1)
    for i in range(1, N + 1):
        if out_visited[i] == 0:
            print('##', i)
            rst += dfs(i)

    print('#', rst)
    continue
