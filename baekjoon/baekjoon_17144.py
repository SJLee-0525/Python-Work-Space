import sys

def find_mc(R):
    '''공기청정기 위치를 찾는 함수'''
    for i in range(R):
        if room[i][0] == -1:
            return (i, 0), (i + 1, 0)
            # 공기청정기 윗 부분의 좌표 값과 아랫 부분의 좌표 값을 반환


def find_dust(R, C):
    '''먼치를 찾고, 그 먼지를 확산시키는 함수를 작동시키는 함수'''
    global room

    air = [[0] * C for _ in range(R)] # 원본 room과 크기가 같은 air 배열을 생성해주고
    air[H[0]][H[1]] = air[L[0]][L[1]] = -1  # 공기청정기를 표시

    # room을 돌면서 먼지를 찾으면
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                scatter(i, j, R, C, air) # 확산 함수 호출

    room = air # air에 확산된 정보가 모두 들어가면 air가 room을 대체


def scatter(i, j, R, C, air):
    '''먼지를 확산시키는 함수'''
    cnt = 0 # 몇 군데로 확산됐는지 확인하는 카운트

    for k in range(4): # 델타를 이용해 주변 탐색
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < R and 0 <= mj < C and room[mi][mj] != -1: # index 범위를 벗어나지 않고, 해당 위치가 공기청정기가 아니라면
            air[mi][mj] += room[i][j] // 5  # 먼지 확산해주고
            cnt += 1                        # 카운트 증가
    air[i][j] += (room[i][j] - ((room[i][j] // 5) * cnt))   # 먼지가 다 확산되고 나면, 확산된 양에 따라서 원래 위치의 값 할당


def cleaning(H, L, R, C):
    '''공기청정기가 작동했을 때의 상황을 구현하는 함수
    정방향으로 구현하는 모습이 딱히 생각이 안 나서, 작동 방향과는 달리 역으로 도는 형태로 구현'''
    global room # room 자체를 바꿀 것임

    i1, j1, k1 = H[0] - 1, H[1], 0 # 위쪽 공기청정기 작동 시작점과 기본 델타 값 할당

    while 1: # 델타 순회
        mi_1, mj_1 = i1 + ci[k1], j1 + cj[k1]

        if mi_1 == H[0] and mj_1 == H[1]: # 다음 위치가 만약 공기청정기라면
             room[i1][j1] = 0   # 새 바람이 나오는 곳이므로 0으로 바꿔주고
             break              # 해당 while문 종료
        elif 0 <= mi_1 <= H[0] and 0 <= mj_1 < C: # 다음 위치가 위쪽 공기청정기의 청소 범위를 벗어나지 않는다면
            room[i1][j1] = room[mi_1][mj_1] # 현재 위치의 값을 다음 위치의 값으로 바꿔주고 (순환)
            i1, j1 = i1 + ci[k1], j1 + cj[k1] # 이동
        else:   # 해당되지 않는다면 방향 전환
            k1 += 1

    i2, j2, k2 = L[0] + 1, L[1], 2 # 아래쪽 공기청정기 작동 시작점과 기본 델타 값 할당

    while 1: # 델타 순회
        mi_2, mj_2 = i2 + ci[k2], j2 + cj[k2]

        if mi_2 == L[0] and mj_2 == L[1]: # 다음 위치가 만약 아래쪽 공기청정기라면
             room[i2][j2] = 0   # 새 바람이 나오는 곳이므로 0으로 바꿔주고
             break              # 해당 while문 탈출
        elif L[0] <= mi_2 < R and 0 <= mj_2 < C: # 다음 위치가 아래쪽 공기청정기의 청소 범위를 벗어나지 않는다면
            room[i2][j2] = room[mi_2][mj_2] # 현재 위치의 값을 다음 위치의 값으로 바꿔주고 (순환)
            i2, j2 = i2 + ci[k2], j2 + cj[k2] # 이동
        else:   # 해당되지 않는다면 방향 전환
            k2 = (k2 + 3) % 4


def cnt_dust(R, C):
    '''마지막 순간 먼지의 양을 카운트 하는 함수'''
    cnt = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j] != 0: # 공기청정기랑, 빈 공간이 아니면
                cnt += room[i][j]   # 값 추가
    
    return cnt

###############################################################################

R, C, T = map(int, sys.stdin.readline().split()) # 세로, 가로, 시간

room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 먼지 확산용 델타
di = [1, 0, -1, 0] 
dj = [0, 1, 0, -1]

# 공기청정기 작동용 델타
ci = [-1, 0, 1, 0]
cj = [0, 1, 0, -1]

H, L = find_mc(R) # (2, 0) (3, 0)
# H: 공기 청정기의 위쪽, L: 아래쪽

for _ in range(T):          # T초 만큼
    find_dust(R, C)         # 먼지를 찾아 확산시키고
    cleaning(H, L, R, C)    # 공기청정기를 작동시켜 순환시킴

print(cnt_dust(R, C))