def dfs(st):
    stack = []
    checked[st] = 1
    while 1:
        for w in adjL[st]:
            if checked[w] == 0:
                stack.append(st)
                st = w
                checked[st] = 1
                break
        else:
            if stack:
                st = stack.pop()
            else:
                return

##################################################################

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # 출석번호, 신청서 수
    arr = list(map(int, input().split())) # 신청서 나열
    adjL = [[] for _ in range(N + 1)] # 신청서 뽑아와서
    for i in range(M):
        p1, p2 = arr[i * 2], arr[i * 2 + 1]
        adjL[p1].append(p2) # 양방향으로 경로 생성
        adjL[p2].append(p1)

    checked = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not checked[i]: # 체크된 적 없으면
            cnt += 1       # 조 개수 늘려주고
            dfs(i)         # dfs 탐색

    print(f'#{tc} {cnt}')