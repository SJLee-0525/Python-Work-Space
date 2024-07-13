t = int(input())

for tt in range(t):
    n = int(input())

    box = []
    for _ in range(n):
        b = list(map(int, input().split()))
        box.append(b)

    box_90 = []
    for _ in range(n):
        box_90.append([0] * n)

    box_180 = []
    for _ in range(n):
        box_180.append([0] * n)

    box_270 = []
    for _ in range(n):
        box_270.append([0] * n)

    for i in range(n):
        for j in range(n):
            box_90[i][j] = box[n - 1 - j][i]

    for i in range(n):
        for j in range(n):
            box_180[i][j] = box_90[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            box_270[i][j] = box_180[n - 1 - j][i]

    print(f'#{tt + 1}')
    for i in range(n):
        for a in range(n):
            print(box_90[i][a], end = '')
        print(' ', end = '')

        for b in range(n):
            print(box_180[i][b], end = '')
        print(' ', end = '')

        for c in range(n):
            print(box_270[i][c], end = '')
        print(' ')
