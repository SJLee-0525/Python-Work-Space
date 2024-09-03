import sys

def find_cctv(N, M):
    '''cctv 좌표와 정보를 저장하는 함수'''
    for i in range(N):
        for j in range(M):
            if 1 <= office[i][j] <= 5:  # 해당 좌표에 cctv가 있으면
                cctv_list.append((i, j, office[i][j])) # 좌표 값이랑, cctv 정보 리스트에 삽입

def surveil(index, T, i_office):
    '''감시의 경우 생성'''
    global result
    if index == T:  # 만약 모든 cctv를 다 탐색했으면
        temp = 0    # 사각지대 카운트 변수 할당
        for ii in range(N):
            for jj in range(M):
                if i_office[ii][jj] == 0:
                    temp += 1   # 사각지대 있을 때마다 카운트 하고
        if result > temp:       # 최소값 비교 할당
            result = temp
        return

    n_office = [i[:] for i in i_office] # 입력받은 맵 복제
    i, j, tp = cctv_list[index]         # cctv 정보 불러옴
    if tp == 1:                         # cctv 타입이 1이면
        for k in dir_D[tp]:             # 딕셔너리에서 델타 인덱스 받아와서 델타 순회
            mi, mj = i + di[k], j + dj[k]
            while 0 <= mi < N and 0 <= mj < M and i_office[mi][mj] != 6: # 인덱스를 벗어나지 않고, 벽을 만나지 않는 한
                if i_office[mi][mj] not in dir_D:  # cctv는 지우지 않는 선에서 감시 범위가 닿는 곳에 '#' 표시
                    i_office[mi][mj] = '#'
                mi += di[k]     # 확장
                mj += dj[k]
            surveil(index + 1, T, i_office)     # 만들어진 맵으로 다음 재귀 호출
            i_office = [n[:] for n in n_office] # 다음 k 반복을 위한 맵 복구
    elif tp in [2, 3, 4]:               # 이하 동일
        for l in dir_D[tp]:
            for k in l:
                mi, mj = i + di[k], j + dj[k]
                while 0 <= mi < N and 0 <= mj < M and i_office[mi][mj] != 6:
                    if i_office[mi][mj] not in dir_D:
                        i_office[mi][mj] = '#'
                    mi += di[k]
                    mj += dj[k]
            surveil(index + 1, T, i_office)     # 재귀 호출
            i_office = [n[:] for n in n_office] # 맵 복구
    elif tp == 5:
        for k in dir_D[tp]:
            mi, mj = i + di[k], j + dj[k]
            while 0 <= mi < N and 0 <= mj < M and i_office[mi][mj] != 6:
                if i_office[mi][mj] not in dir_D:
                    i_office[mi][mj] = '#'
                mi += di[k]
                mj += dj[k]
        surveil(index + 1, T, i_office) # 얘는 다음 탐색을 위한 맵 복구를 할 필요가 없긴 함

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# cctv별 델타 인덱스 타입 정리한 딕셔너리
dir_D = {1: [0, 1, 2, 3],
         2: [[0, 2], [1, 3]],
         3: [[3, 0], [0, 1], [1, 2], [2, 3]],
         4: [[2, 3, 0], [3, 0, 1], [0, 1, 2], [1, 2, 3]],
         5: [0, 1, 2, 3]}

N, M = map(int, sys.stdin.readline().split()) # N 세로, M 가로
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# cctv 찾아서 리스트에 정보 추가
cctv_list = []
find_cctv(N, M)

# 감시의 경우 탐색 호출
result = 1000
surveil(0, len(cctv_list), office)

print(result)