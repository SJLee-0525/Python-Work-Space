import sys

di = [-1, -1]
dj = [1, -1]

def check(si, sj):
    for y in range(N):
        if arr[y][sj] == 1:
            return False

    for k in range(2):
        mi, mj = si + di[k], sj + dj[k]
        while 0 <= mi < N and 0 <= mj < N:
            if arr[mi][mj] == 1:
                return False
            mi += di[k];
            mj += dj[k];

    return True

def putQueen(lv):
    global cnt

    if lv == N:
        cnt += 1
        return

    for i in range(N):
        if used[i]:
            continue
        if check(lv, i):
            arr[lv][i] = 1
            used[i] = 1
            putQueen(lv + 1)
            arr[lv][i] = 0
            used[i] = 0

##############################################

N = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]

cnt = 0
used = [0] * N
putQueen(0)

print(cnt)