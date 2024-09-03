import sys

def garo(i, j, X, Y):
    '''ㅡ 모양 폴리오미노'''
    if j + 3 < X:
        return arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
    return 0

def nemo(i, j, X, Y):
    '''정사각형 폴리오미노'''
    if i + 1 < Y and j + 1 < X:
        return arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
    return 0

def nien(i, j, X, Y):
    '''L 폴리오미노'''
    if i + 2 < Y and j + 1 < X:
        return arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
    return 0

def liel(i, j, X, Y):
    '''꺽쇠 폴리오미노'''
    if i + 2 < Y and j + 1 < X:
        return arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    return 0

def fck(i, j, X, Y):
    '''ㅜ 폴리오미노'''
    if i + 1 < Y and j + 2 < X:
        return arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2]
    return 0

##################################################################################

N, M = map(int, sys.stdin.readline().split()) # N 세로, M 가로
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []
rt_cnt = 0  # 회전 횟수 카운트
while rt_cnt <= 3:
    temp = [a[:] for a in arr]      # 기본 배열 저장
    for i in range(N):
        for j in range(M):
            result.append(garo(i, j, M, N))
            result.append(nemo(i, j, M, N))
            result.append(nien(i, j, M, N))
            result.append(liel(i, j, M, N))
            result.append(fck(i, j, M, N))

    arr = [a[::-1] for a in arr]    # 배열 뒤집기 (좌우)
    for i in range(N):              # 여기서는 ㅡ과 ㅁ은 굳이 검사 안 함 (좌우 대칭)
        for j in range(M):
            result.append(nien(i, j, M, N))
            result.append(liel(i, j, M, N))
            result.append(fck(i, j, M, N))

    arr = [a[:] for a in temp]          # 임시로 저장해둔 배열 가져옴
    temp_rotate = zip(*arr[::-1])       # 배열 회전
    arr = [t[:] for t in temp_rotate]   # arr에 재할당
    N, M = M, N                         # N, M 뒤바꾸고
    rt_cnt += 1                         # 로테이트 횟수 증가

print(max(result))