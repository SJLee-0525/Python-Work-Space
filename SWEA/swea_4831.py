T = int(input())

for test in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K = 한 번 충전으로 이동할 수 있는 거리
    # N = 종점
    # M = 충전기 수 수
    gas_stations = list(map(int, input().split()))
    oil = K
    location = 0
    charge_count = 0
    judge = True
    
    for i in range(len(gas_stations)):
        while location <= N:
            location += 1
            oil -= 1
            if i < len(gas_stations) - 1:
                if location == gas_stations[i]:
                    if location + oil >= gas_stations[i + 1]:
                        break
                    elif location + K >= gas_stations[i + 1]:
                        oil = K
                        charge_count += 1
                        break
                    elif location + K < gas_stations[i + 1]:
                        judge = False     
                        break
            else:
                if location == gas_stations[i]:
                    if location + oil >= N:
                        break
                    elif location + K >= N:
                        oil = K
                        charge_count += 1
                        break
                    elif location + K < N:
                        judge = False
                        break

    if judge == False:
        charge_count = 0

    print(f'#{test} {charge_count}')
    
        
