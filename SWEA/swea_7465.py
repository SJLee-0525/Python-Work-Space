def dfs(s):
    stack = []
    checked[s] = 1
    while 1:
        for w in adj_P[s]:
            if not checked[w]:  # 확인되지 않은 사람이면
                stack.append(s)
                s = w
                checked[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                return

##############################################################################

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # 마을 주민 수, 관계 간선 수

    adj_P = [[] for _ in range(N + 1)]
    for _ in range(M):
        r1, r2 = map(int, input().split())
        adj_P[r1].append(r2)
        adj_P[r2].append(r1)

    cnt = 0
    checked = [0] * (N + 1)
    for p in range(1, N + 1):
        if not checked[p]:  # 만약 확인되지 않은 사람이면
            dfs(p)          # dfs 탐색으로 그 사람과 연결된 사람들을 확인
            cnt += 1        # 탐색할 때마다 그룹 개수 증가

    print(f'#{tc} {cnt}')