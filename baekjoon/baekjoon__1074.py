import sys

def Z_search(si, sj, ei, ej, lev, r, c, N, min_val, max_val):
    # if si > r and sj > c: # 가지치기 (찾고자 하는 좌표보다 더 큰 곳은 탐색할 필요 없음)
    #     return
    # if ei < r and ej < c:
    #     return
    if lev == N - 1: # 최대 레벨에 도달했을 때 (2 * 2 배열이 되면)
        global rst
        if si <= r < ei and sj <= c < ej:
            cnt = -1
            for i in range(si, ei):
                for j in range(sj, ej):
                    cnt += 1
                    if i == r and j == c:
                        rst = min_val + cnt
        return

    # 최대 레벨에 도달하지 않았다면 (배열의 각 사이즈가 2보다 크다면)
    mi = (si + ei) // 2 # 중간 값 지정
    mj = (sj + ej) // 2
    '''
    1 2
    3 4
    '''
    # 위 주석 순으로 박스를 쪼개어 재귀 호출
    # 다 돌리니까 시간초과 메모리초과 난리남.
    # 입력받은 조건에 부합하는 재귀만 돌려보자.
    if si <= r < mi and sj <= c < mj:   # 1
        Z_search(si, sj, mi, mj, lev + 1, r, c, N, min_val, min_val + max_val * 0.25)
    elif si <= r < mi and mj <= c < ej: # 2
        Z_search(si, mj, mi, ej, lev + 1, r, c, N, min_val + (max_val - min_val) * 0.25, min_val + max_val * 0.5)
    elif mi <= r < ei and sj <= c < mj: # 3
        Z_search(mi, sj, ei, mj, lev + 1, r, c, N, min_val + (max_val - min_val) * 0.5, min_val + max_val * 0.75)
    elif mi <= r < ei and mj <= c < ej: # 4
        Z_search(mi, mj, ei, ej, lev + 1, r, c, N, min_val + (max_val - min_val) * 0.75, max_val)

#####################################################################################

N, r, c = map(int, sys.stdin.readline().split())

arr_len = 1 << N
# arr = [[0] * arr_len for _ in range(arr_len)] # <<< 배열 쓰니까 메모리 초과남 << 배열 안쓰니 시간 초과남 하..

cnt = -5
rst = 0
Z_search(0, 0, arr_len, arr_len, 0, r, c, N, 0, arr_len * arr_len)

# print(arr)
print(int(rst))