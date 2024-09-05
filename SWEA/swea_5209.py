def cal_cost(t_cost, lev, N):
    global min_cost
    if lev == N: # 끝까지 다 탐색하면
        if min_cost > t_cost: # 최소 비용과 비교 후 재할당
            min_cost = t_cost
        return
    if t_cost > min_cost:     # 만약 중간에 최소비용 초과하면 탐색 중단
        return
    for p in range(N):
        if p in calculated: # 다른 방식으로 검사
            continue
        calculated.append(p) # 사용 표시하고
        cal_cost(t_cost + cost_board[lev][p], lev + 1, N) # 다음 단계로 재귀 호출
        calculated.pop() # 사용 표시 취소

#######################################################################

for tc in range(1, int(input()) + 1):
    N = int(input()) # 제품 수
    cost_board = [list(map(int, input().split())) for _ in range(N)]
    calculated = []

    min_cost = 10001
    cal_cost(0, 0, N)

    print(f'#{tc} {min_cost}')