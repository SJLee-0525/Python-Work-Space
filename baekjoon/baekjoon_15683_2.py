import sys

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cctvDirDict = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def findCctvLoc():
    '''최초에 사무실을 순회하며, 빈 블록의 개수를 세고, cctv가 있는 곳의 좌표 수를 셈'''
    cnt = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:   # 빈 공간
                cnt += 1
            elif office[i][j] < 6:  # cctv
                cctvList.append((i, j))
    return cnt

def servail(lv, blindSpotCnt):
    '''각 cctv마다 모든 경우의 수를 돌리며 재귀 호출'''
    global result

    # 모든 cctv를 다 탐색했으면 최소값 비교 후 할당
    if lv == len(cctvList):
        result = min(blindSpotCnt, result)
        return

    i, j = cctvList[lv] # 해당 lv(index)에 있는 cctv 좌표 가져옴
    for info in cctvDirDict[office[i][j]]:  # 해당 cctv 타입에 따른 딕셔너리 value 값 가져오고
        cnt, changedLoc = 0, []             # 감시 당하는 좌표 개수, 감시 당하는 좌표 담을 리스트
        for k in info:                      # 델타 순회
            mi, mj = i + di[k], j + dj[k]
            # 범위를 벗어나지 않고, 해당 좌표가 벽을 만나기 전까지 반복
            while 0 <= mi < N and 0 <= mj < M and office[mi][mj] != 6:
                if office[mi][mj] == 0:         # 만약 벽도 cctv도 아니라면
                    cnt += 1                    # 감시 카운트 증가
                    office[mi][mj] = -1         # 감시 표시
                    changedLoc.append((mi, mj)) # 해당 좌표 감시 좌표 리스트에 담음 (맵 복구 위해)
                # 이동
                mi += di[k]
                mj += dj[k]

        servail(lv + 1, blindSpotCnt - cnt) # lv 값을 올리고, 빈 블록의 개수를 계산해 재귀 호출

        # 맵 복구) 감시 좌표 리스트에 담긴 좌표 값을 뽑아서 해당 좌표 0으로 복구
        while changedLoc:
            ci, cj = changedLoc.pop()
            office[ci][cj] = 0

##############################################################################

N, M = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cctvList = []
blindSpots = findCctvLoc()

result = 10000001
servail(0, blindSpots)

print(result)