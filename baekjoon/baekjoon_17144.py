import sys

def find_mc(R):
    for i in range(R):
        if room[i][0] == -1:
            return (i, 0), (i + 1, 0)

def find_dust(R, C):
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                scatter(i, j, R, C)

def scatter(i, j, R, C):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    cnt = 0
    for k in range(4):
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < R and 0 <= mj < C and room[mi][mj] != -1:
            air[mi][mj] += room[i][j] // 5
            cnt += 1
        air[i][j] = room[i][j] - ((room[i][j] // 5) * cnt)



R, C, T = map(int, sys.stdin.readline().split())
# 세로, 가로, 시간
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air = [[0] * C for _ in range(R)]

H, L = find_mc(R) # (2, 0) (3, 0)

find_dust(R, C)
print(air)
