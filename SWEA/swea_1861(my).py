di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    adj_B = [0] * ((N ** 2) + 1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                mi, mj = i + di[k], j + dj[k]
                if 0 <= mi < N and 0 <= mj < N and room[i][j] + 1 == room[mi][mj]:
                    adj_B[room[i][j]] += 1
                    break

    max_cnt = cnt = start = 0
    for r in range(N**2 - 1, -1, -1):
        if adj_B[r]:
           cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = r + 1
            cnt = 0

    print(f'#{tc} {start} {max_cnt + 1}')