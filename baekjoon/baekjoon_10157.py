# 달팽이 배열 문제
import sys

X, Y = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

if X * Y < K:
    print(0)

else:
    seats = [[0] * X for _ in range(Y)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    i, j, k = 0, 0, 0

    for person in range(1, K + 1):
        seats[i][j] = person
        if person == K:
            break
        if 0 <= i + di[k] < Y and 0 <= j + dj[k] < X and seats[i + di[k]][j + dj[k]] == 0:
            i += di[k]
            j += dj[k]
        else:
            k = (k + 1) % 4
            i += di[k]
            j += dj[k]

    # count = 1
    # while count <  K:
    #     seats[i][j] = count
    #     if 0 <= i + di[k] < Y and 0 <= j + dj[k] < X and seats[i + di[k]][j + dj[k]] == 0:
    #         i += di[k]
    #         j += dj[k]
    #         count += 1
    #     else:
    #         k += 1
    #         if k == 4:
    #             k = 0
    
    print(j + 1, i + 1)


