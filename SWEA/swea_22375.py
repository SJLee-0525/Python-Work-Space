for tc in range(1, int(input()) + 1):
    N = int(input())
    init_bulb = list(map(int, input().split()))
    fin_bulb = list(map(int, input().split()))

    std = 0
    cnt = 0
    for i in range(N):
        if fin_bulb[i] != init_bulb[i]:
            cnt += 1
            for j in range(i, N):
                if init_bulb[j] == 0:
                    init_bulb[j] = 1
                else:
                    init_bulb[j] = 0
        if init_bulb == fin_bulb:
            break

    print(f'#{tc} {cnt}')