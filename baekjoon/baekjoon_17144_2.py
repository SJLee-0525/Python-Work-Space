import sys

# 델타, 상단 공기청정기는 0부터 +1 / 하단 공기청정기는 2부터 -1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def findAirPurifier():
    '''공기 청정기 상/하단 좌표 반환'''
    for i in range(R):
        if room[i][0] == -1:
            return i, i + 1

def findDust():
    '''먼지 위치 찾고, 먼지 확산 함수 호출'''
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:  # 먼지가 있으면
                diffuseDust(i, j, room[i][j])

def diffuseDust(i, j, dust):
    '''먼지 확산'''
    dir = 0 # 확산 가능한 방향 수 계산

    for k in range(4):
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < R and 0 <= mj < C and room[mi][mj] >= 0:
            temp[mi][mj] += dust // 5   # 임시 배열에 확산한 값 추가
            dir += 1                    # 방향 수 카운트

    temp[i][j] += dust - (dust // 5) * dir  # 원래 먼지 있던 곳은 빠진 만큼 제거후 임시 배열에 추가

def operateAirPurifier():
    '''
    공기 청정기 작동
    정방향 순회는 구현 방법이 떠오르지 않아, 역방향으로 구현
    '''
    # TOP
    ti, tj, topDir = top - 1, 0, 0  # 공기 청정기 상단보다 한 칸 위 할당, 델타에 사용할 방향 값
    while 1:
        mi, mj = ti + di[topDir], tj + dj[topDir]
        if 0 <= mi < R and 0 <= mj < C and mi <= top: # 범위 벗어나지 않는 선에서
            if temp[mi][mj] == -1:  # 만약 공기청정기로 돌아왔다면
                temp[ti][tj] = 0    # 깨끗한 공기 할당 후 중단
                break
            temp[ti][tj] = temp[mi][mj] # 먼지 이동
            ti, tj = mi, mj             # 기준 좌표 이동
        else:
            topDir = (topDir + 1) % 4   # 해당 방향으로 더 갈 수 없다면 방향 전환

    # BOTTOM
    bi, bj, botDir = bottom + 1, 0, 2   # 공기 청정기 하단보다 한 칸 아래 할당, 델타에 사용할 방향 값
    while 1:
        mi, mj = bi + di[botDir], bj + dj[botDir]
        if 0 <= mi < R and 0 <= mj < C and mi >= bottom:
            if temp[mi][mj] == -1:  # 만약 공기청정기로 돌아왔다면
                temp[bi][bj] = 0    # 깨끗한 공기 할당 후 중단
                break
            temp[bi][bj] = temp[mi][mj] # 먼지 이동
            bi, bj = mi, mj             # 기준 좌표 이동
        else:
            botDir = (botDir - 1) % 4   # 해당 방향으로 더 갈 수 없다면 방향 전환

def next():
    '''완성한 temp 배열을 room으로 복사 및 temp 배열 초기화'''
    for i in range(R):
        for j in range(C):
            room[i][j] = temp[i][j] # room에 계산한 temp 배열 복사
            temp[i][j] = 0          # temp 초기화

    temp[top][0] = temp[bottom][0] = -1 # temp에 공기청정기 할당

def calDustAmount():
    '''미세먼지 총합 계산'''
    amount = 2          # 공기청정기 고려
    for i in range(R):
        for j in range(C):
            amount += room[i][j]

    return amount

###################################################################

R, C, T = map(int, sys.stdin.readline().split())
# R * C / T초 후의 미세먼지 양

# 방 미세먼지 정보 입력
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

top, bottom = findAirPurifier()     # 공기 청정기 윗단, 아랫단 계산

# 값 계산에 사용할 임시 배열 생성
temp = [[0] * C for _ in range(R)]
temp[top][0] = temp[bottom][0] = -1 # 공기청정기 좌표 할당

for _ in range(T):  # T초 동안
    findDust()              # 먼지 찾고 확산하는 함수
    operateAirPurifier()    # 공기 청정기 작동
    next()                  # room에 temp 배열 복사 및 temp 초기화

result = calDustAmount()
print(result)


