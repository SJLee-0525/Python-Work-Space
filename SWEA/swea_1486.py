def combi(N):
    '''조합 만들어서 각 경우 더해보기'''
    global min_H
    for i in range(1 << N):
        s = 0               # 탑 높이
        for j in range(N):
            if i & (1 << j):
                s += P[j]
                if s >= min_H: # 넘어서면 해당 경우는 중단
                    break
        if s >= B:          # 만약 선반보다 탑이 더 높은데
            if min_H > s:   # 최소 값이라면
                min_H = s   # 갱신

###################################################

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    P = list(map(int, input().split()))

    min_H = 10000000
    combi(len(P))

    print(f'#{tc} {min_H - B}')  # 차이 출력