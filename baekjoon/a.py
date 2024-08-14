T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    judge = False
    cross_1 = 0
    cross_2 = 0
    for i in range(N):
        garo = 0
        sero = 0
        for j in range(N):
            if arr[i][j] == 'o':
                garo += 1
                if garo >= 5:
                    judge = True
            if arr[i][j] == '.':
                garo = 0

            if arr[j][i] == 'o':
                sero += 1
                if sero >= 5:
                    judge = True
            if arr[j][i] == '.':
                sero = 0

    for ii in range(N):
        cross_1 = 0
        for jj in range(N - ii):
            if arr[jj][ii + jj] == 'o':
                    cross_1 += 1
                    if cross_1 >= 5:
                        judge = True
            elif arr[jj][ii + jj] == '.':
                cross_1 = 0

    for st in range((N - 1) * 2 + 1):
        cross_2 = 0
        for iii in range(N):
            for jjj in range(N):
                if iii + jjj == st:
                    if arr[iii][jjj] == 'o':
                        cross_2 += 1
                        if cross_2 >= 5:
                            judge = True
                elif arr[iii][jjj] == '.':
                    cross_2 = 0

    if judge == True:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')