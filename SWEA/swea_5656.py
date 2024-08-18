from collections import deque

def bomb(idx, N, input_map):
    '''bomb(현재 쏜 횟수, 총 쏴야하는 횟수, 지도)'''
    global cnt_list
    if idx == N: # 만약 총 쏴야하는 횟수에 도달하면 종료 조건으로 남아있는 블록의 개수를 셈
        cnt = 0
        for fi in range(H):
            for fj in range(W):
                if input_map[fi][fj]:
                    cnt += 1
        cnt_list.append(cnt)
        return
    else:   # 종료 조건이 아니라면
        for j in range(W):  # 너비를 먼저
            B = False
            for i in range(H):  # 높이를 후에
                if input_map[i][j] >= 1: # 만약 가장 위의 블록을 발견하면 BFS 탐색 시작
                    # init_map = copy.deepcopy(input_map)
                    init_map = [new[:] for new in input_map] # deepcopy와 유사하게 쓸 수 있음 (좀 더 빠르다는 듯)
                    Q = deque()
                    Q.append((i, j, input_map[i][j]))
                    while Q:
                        ii, jj, value = Q.popleft()
                        if value == 1: # 만약 1이면 자기 자신만 소멸되므로
                            input_map[ii][jj] = 0
                        elif value >= 2: # 연쇄 반응 일으키는 애들
                            input_map[ii][jj] = 0 # 본인은 바꿔줌
                            di = [1, 0, -1, 0]
                            dj = [0, 1, 0, -1]
                            for k in range(4): # 델타 순회
                                for l in range(1, value): # 해당 블록의 값만큼 추가 터짐
                                    mi, mj = ii + (di[k] * l), jj + (dj[k] * l)
                                    if 0 <= mi < H and 0 <= mj < W and input_map[mi][mj] != 0 and (mi, mj, input_map[mi][mj]) not in Q:
                                        Q.append((mi, mj, input_map[mi][mj])) # 일으키는 애들을 다 큐에 넣음
                    # 블록 내리기
                    new_map = [[0] * W for _ in range(H)]   # 빈 새 지도를 만들고
                    for jjj in range(W):
                        temp_v = [] # 값이 있는 애들을 임시 리스트에 담고
                        for iii in range(H):
                            if input_map[iii][jjj] >= 1:
                                temp_v.append(input_map[iii][jjj])
                        for vi in range(len(temp_v)): # 임시 리스트에 있는 애들을 위치에 맞게 내려 새 지도에 담음
                            new_map[H - len(temp_v) + vi][jjj] = temp_v[vi]

                    B = True # 맨 위만 탐색해야 함: 탐색을 거쳤으니 변수를 바꿔서 다음 탐색을 하지 못하도록 만듦

                if B == True: # 한 번 탐색했다면, 변한 맵을 가지고서 재귀 호출
                    bomb(idx + 1, N, new_map)
                    input_map = init_map
                    break

    bomb(N, N, input_map) # 여기까지 오면 벽돌이 없다는 뜻. N을 idx에 대입시켜 강제로 종료 조건을 만들어 줌

####################################################################################################

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split()) # 쏘는 횟수, 너비, 높이
    block_map = [list(map(int, input().split())) for _ in range(H)]
    cnt_list = []
    bomb(0, N, block_map)
    print(f'#{tc} {min(cnt_list)}')

