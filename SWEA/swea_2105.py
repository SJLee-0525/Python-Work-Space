# visited 안 만들어도 존나 잘 돌아가는듯 , 왜?
    # 애초에 구조 자체가 visited 필요 없을 것 같긴 함
# 아니 조건 달아주는데 왜 갈 수록 느려지ㅡㄴㄴ데

def walking(si, sj, i, j, cnt, dir, des_type=None):
    '''
    재귀를 기반으로 대각선 순회
    walking(시작 좌표, 현재 좌표, 먹은 개수 카운트, 방향, visited, 지금까지 먹은 디저트 종류)
    '''
    global max_V

    '''
    [시작 조건] 첫 호출 시 시작 조건 생성
    '''
    # if visited == None:  # 처음 호출되면 visited를 생성하고
    #     visited = [[0] * N for _ in range(N)]
    #     visited[si][sj] = 1  # 방문 표시
    if des_type == None:  # 처음 호출되면 지금까지 먹은 디저트 종류를 담을 리스트 생성
        des_type = []

    '''
    [종료 조건] 방향이 3 이상이고 시작 좌표랑 현재 좌표랑 같다면 :
    방향 조건 넣은 이유: 안 넣으면 시작하자마자 끝남 ㅋㅋ
    '''
    if (si, sj) == (i, j) and dir >= 3:
        if max_V < cnt:  # 카운트 한 개수랑 현재의 최대 값 비교 후
            max_V = cnt  # 갱신
        return

    # 애초에 재귀 호출하기 전에 조건을 달아주고 가니까 굳이 여기서 달 게 없음

    cnt += 1  # 방문하면 먹은 디저트 수 카운트 해주고

    '''[재귀 호출]'''
    mi, mj = i + di[dir], j + dj[dir]  # 현재 방향을 유지하는 조건으로 다음 좌표 값을 계산
    if 0 <= mi < N and 0 <= mj < N and cafe_road[mi][mj] not in des_type:
        # 만약 유지한 채로 갈 수 있고, 다음 위치의 디저트가 아직 먹지 않은 디저트이면
        des_type.append(cafe_road[mi][mj])  # 다음 디저트를 먹은 종류 리스트에 담고
        # visited[mi][mj] = 1  # 방문 표시 후
        walking(si, sj, mi, mj, cnt, dir, des_type)  # 다음 좌표로 재귀 호출
        # visited[mi][mj] = 0  # 다시 지워줌
        des_type.pop()  # 먹은 것도 뽑아냄

    if dir + 1 < 4:  # 아직 만약 방향을 바꿀 수 있다면
        mi, mj = i + di[dir + 1], j + dj[dir + 1]  # 바꾼 방향으로 다음 좌표 값 계산해보고
        if 0 <= mi < N and 0 <= mj < N and cafe_road[mi][mj] not in des_type:
            # 방향을 바꾸고서 다음 좌표에 갈 수 있고, 다음 위치의 디저트가 아직 먹지 않은 디저트이면
            des_type.append(cafe_road[mi][mj])  # 다음 디저트를 먹은 종류 리스트에 담고
            # visited[mi][mj] = 1  # 방문 표시 후
            walking(si, sj, mi, mj, cnt, dir + 1, des_type)  # 다음 좌표로 재귀 호출
            # visited[mi][mj] = 0  # 다시 지워줌
            des_type.pop()  # 먹은 것도 뱉어냄

################################################################################

# 델타
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

################################################################################

for tc in range(1, int(input()) + 1):
    N = int(input())  # 지역 한 변의 길이
    cafe_road = [list(map(int, input().split())) for _ in range(N)]

    max_V = 0
    for i in range(N):
        for j in range(N):
            if 0 <= j - 1 and j + 1 < N:  # 오른쪽 아래 / 좌측 아래로 탐색을 시작할 수 있을 경우에만
                walking(i, j, i, j, 0, 0)  # 탐색 함수 호출

    if max_V >= 1:
        print(f'#{tc} {max_V}')
    else:
        print(f'#{tc} -1')