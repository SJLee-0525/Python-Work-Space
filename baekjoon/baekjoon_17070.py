import sys

def find_r(i, j, N, type):
    global cnt
    if (i, j) == (N - 1, N - 1): # 도착하면 cnt 증가
        cnt += 1
    else:
        if type != 2 and 0 <= j + dj[0] < N and room[i][j + dj[0]] == 0:
            # 가로로 가는 공간이 비어있고, 현재 진행 방향이 세로가 아니라면
            mj = j + dj[0]
            # 이동시키고 재귀 호출
            find_r(i, mj, N, 0)
        if 0 <= i + di[1] < N and 0 <= j + dj[1] < N and room[i + di[1]][j] == room[i][j + dj[1]] == room[i + di[1]][j + dj[1]] == 0:
            # 대각선으로 가는 조건에 맞고(우,하,우하단이 비어있다면)
            mi, mj = i + di[1], j + dj[1]
            # 이동시키고 재귀 호출
            find_r(mi, mj, N, 1)
        if type != 0 and 0 <= i + di[2] < N and room[i + di[2]][j] == 0:
            # 세로로 가는 공간이 비어있고, 현재 진행 방향이 가로가 아니라면
            mi = i + di[2]
            # 이동시키고 재귀 호출
            find_r(mi, j, N, 2)
        return

N = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 타입 0: 가로, 1: 대각선, 2: 세로
cnt = 0

di = [0, 1, 1]
dj = [1, 1, 0]

find_r(0, 1, N, 0)
# 출발좌표, N, 출발모양(시작은 가로)

print(cnt)
