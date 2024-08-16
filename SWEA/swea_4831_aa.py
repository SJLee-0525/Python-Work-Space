T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # 최대 이동거리, 종점, 충전기 수
    gas_st_list = list(map(int, input().split()))

    stations = [0] * (N) + [N]
    for gas_st in gas_st_list:
        stations[gas_st] = gas_st

    start, refuel = 0, 0
    while 1:
        end = 0
        # start에서 오른쪽으로 K범위 만큼 탐색
        for i in range(start + 1, start + K + 1):
            if i == N:  # 만약 종점에 도착하면
                end = i # 종점 할당
                break
                # 만약 0이 아닌 값이 있다면
            elif end < stations[i]:
                end = stations[i]
        if end == 0:    # 만약 주유할 수 있는 공간이 없었다면
            print(f'#{tc} 0')
            break
        elif end == N:  # 만약 종점과 같다면 end가
            print(f'#{tc} {refuel}')
            break
        # 그 외에는 주유하고, start 위치를 end로 재할당
        refuel += 1
        start = end
