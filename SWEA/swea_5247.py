from collections import deque

def f(n, M):
    Q = deque()
    Q.append(n)
    visited = [0] * 1000001
    visited[n] = 1


    while Q:
        in_N = Q.popleft()

        if in_N == M:
            return visited[M]

        if in_N + 1 <= 1000000 and visited[in_N + 1] == 0:
            visited[in_N + 1] = visited[in_N] + 1
            Q.append(in_N + 1)
        if in_N - 1 <= 1000000 and visited[in_N - 1] == 0:
            visited[in_N - 1] = visited[in_N] + 1
            Q.append(in_N - 1)
        if in_N * 2 <= 1000000 and visited[in_N * 2] == 0:
            visited[in_N * 2] = visited[in_N] + 1
            Q.append(in_N * 2)
        if in_N - 10 <= 1000000 and visited[in_N - 10] == 0:
            visited[in_N - 10] = visited[in_N] + 1
            Q.append(in_N - 10)

#################################################################

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {f(N, M) - 1}')