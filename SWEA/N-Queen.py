import pprint

def check(i, j, N):
    '''놓기 전 해당 위치가 유망한지 검사하는 함수'''
    for y in range(N):  # 해당 열 검사 (행 검사 퀸 놓기전 하므로 필요 없음)
        if board[y][j] == 1:
            return False

    for k in range(2):  # 대각선 검사 (인접한 대각선만 보는 게 아니라 끝까지 다 봐야함)
        mi, mj = i + di[k], j + dj[k]
        while 0 <= mi < N and 0 <= mj < N:
            if board[mi][mj] == 1:
                return False
            mi += di[k]
            mj += dj[k]

    return True # 문제 없이 다 돌면 true 반환

def put_queen(n, N):
    global cnt
    if n == N:  # 최대 레벨에 도달하면 카운트 증가 후 리턴
        cnt += 1
        return
    for p in range(N):
        if check(n, p, N): # 해당 위치 검사를 통과하면
            board[n][p] = 1 # 퀸 놓고
            put_queen(n + 1, N) # 다음 단계로 재귀 호출
            board[n][p] = 0 # 다음 반복을 위해 되돌림

for tc in range(1,int(input()) + 1):
    N = int(input()) # 퀸의 개수 / 배열 크기
    board = [[0] * N for _ in range(N)]

    di = [-1, -1]
    dj = [-1, 1]

    cnt = 0
    put_queen(0, N)
    print(f'#{tc} {cnt}')