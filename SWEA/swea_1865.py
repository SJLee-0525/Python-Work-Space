def cal_prob(t_cal, i, N):
    global max_prob
    if i == N:
        if max_prob < t_cal:
            max_prob = t_cal
        return
    if max_prob >= t_cal:
        return
    for j in range(N):
        if calculated[j]:
            continue
        calculated[j] += 1
        cal_prob(t_cal * (score_board[i][j] / 100), i + 1, N)
        calculated[j] -= 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    score_board = [list(map(int, input().split())) for _ in range(N)]
    calculated = [0] * N

    max_prob = 0
    cal_prob(1, 0, N)

    result = max_prob * 100
    print(f'#{tc} {result:.6f}')
