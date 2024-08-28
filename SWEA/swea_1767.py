def edge(N):
    '''엣지에 위치한 코어 처리 및 코어 위치 좌표 추가'''
    for i in range(1, N):
        for j in range(1, N):
            if maxinos[i][j] == 1: # 만약 코어가 있는데
                if i == 1 or i == N + 1 or j == 1 or j == N + 1: # 코어가 엣지에 위치하면 이미 연결된 것이니 -1로 바꿈
                    maxinos[i][j] = -1 # 이걸 맨첨에 9로 바꿔서 틀렸음. 주변부도 9로 처리했으니..
                else:   # 만약 주변부에 위치한 코어가 아니면
                    core.append((i, j)) # 코어 리스트에 좌표 추가

def connect_core(index, index_N, N, maxinos, connected_core, wire_len):
    '''코어들을 연결하는 함수'''
    if index == index_N: # 만약 코어 좌표 리스트를 다 탐색했으면
        result.append((connected_core, wire_len))   # 연결된 코어 개수와, 선의 길이를 결과 리스트에 추가
        return

    # 해당 코어를 연결하지 않는 경우를 가정하고 재귀 호출해 다음 탐색
    connect_core(index + 1, index_N, N, maxinos, connected_core, wire_len)

    # 해당 코어를 연결 시도
    i, j = core[index]  # 해당 인덱스의 코어 좌표 불러옴
    for k in range(4):  # 델타 탐색
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < N + 2 and 0 <= mj < N + 2 and maxinos[mi][mj] == 0: # 범위를 벗어나지 않고 그 방향으로 뻗을 수 있다면
            new_maxinos = [m[:] for m in maxinos]   # 맥시노스 맵 복제
            len_cnt = wire_len                      # 선 길이 할당
            while 0 < mi < N + 1 and 0 < mj < N + 1 and new_maxinos[mi][mj] == 0: # 조건에 부합하는 한에서 계속 늘려나감
                new_maxinos[mi][mj] = -1 # 이동한 곳은 연결했다 표시해 주고
                mi += di[k]              # 이동
                mj += dj[k]
                len_cnt += 1             # 선 길이 추가
            if new_maxinos[mi][mj] == 9: # while에서 탈출했는데 코어 끝이면 (해당 좌표 값이 9이면)
                connect_core(index + 1, index_N, N, new_maxinos, connected_core + 1, len_cnt)
                # 해당 코어를 해당 방향으로 연결한 새 맥시노스 맵으로 재귀 호출

##############################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 델타
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    core = []   # 연결되어 있지 않은 core들의 좌표들을 담을 리스트

    # 맥시노스 배열 생성 (기본 제공되는 배열에 9를 감싸서 연산 편하게 만듦)
    # maxinos = [[9] * (N + 2)]
    # for _ in range(N):
    #     row = [9] + list(map(int, input().split())) + [9]
    #     maxinos.append(row)
    # maxinos.append([9] * (N + 2))

    # 리스트 컴프리헨션으로 구현
    maxinos = [[9] * (N + 2)] + \
              [[9] + list(map(int, input().split())) + [9] for _ in range(N)] + \
              [[9] * (N + 2)]

    result = [] # 코어를 연결한 개수와 선의 길이를 담을 결과 리스트

    edge(N)     # 엣지에 있는 코어 처리 및 코어 좌표 추가 함수 호출
    connect_core(0, len(core), N, maxinos, 0, 0)

    result.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    # 결과 리스트 정렬 (정렬 우선순위 1: x[0] - 내림차순 | 2: x[1] 오름차순)

    print(f'#{tc} {result[0][1]}')
