def make_st(i, j, lev, st=None):
    if st == None:
        st = str(arr[i][j])

    if lev == 6:
        rst_s.add(st)
        return

    for k in range(4):
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < 4 and 0 <= mj < 4:
            make_st(mi, mj, lev + 1, st + str(arr[mi][mj]))

###########################################################

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    rst_s = set()
    for i in range(4):
        for j in range(4):
            make_st(i, j, 0)

    # print(rst_s)
    print(f'#{tc} {len(rst_s)}')