def ruun(start, bat, cnt):
    global result
    if start + bat >= N - 1: # 현재 출발점에서 목적지까지 갈 수 있다면
        if result > cnt:     # 최소값과 비교 후 할당
            result = cnt
        return
    if result < cnt:         # 현재 최소값보다 카운트가 커지면
        return               # 리턴
    for n in range(start + 1, start + bat + 1): # 현재 위치에서 갈 수 있는 범위
        ruun(n, battery[n], cnt + 1)      # 범위 내의 위치를 시작점으로 재귀 호출

for tc in range(1, int(input()) + 1):
    N, *battery = map(int, input().split())
    battery = battery + [0]

    result = 10000
    ruun(0, battery[0], 1)

    print(f'#{tc} {result - 1}')