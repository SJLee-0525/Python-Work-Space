def move(input_D):
    '''이동 명령 수행'''
    new_D = {}      # 새롭게 값 담을 새 딕셔너리 생성
    need_check = {} # check가 필요한 경우 데이터를 담을 딕셔너리 생성

    for k, v in input_D.items(): # 입력받은 좌표 딕셔너리를 순회
        i, j = k    # key에서 좌표값 받고
        Q, dir = v  # value에서 미생물 정보 받음
        mi, mj = i + di[dir], j + dj[dir]   # 받은 방향 정보를 이용해서 새 좌표값 계산
        if mi in [0, N - 1] or mj in [0, N - 1]: # 만약 약품 있는 곳에 도달하면
            Q //= 2 # 미생물의 수는 2로 나는 몫으로 줄임
            if Q == 0: # 만약 미생물 수가 0이 되면 건너뜀
                continue
            if dir == 1: # + 방향을 반대로 바꿔줌
                dir = 2
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 4
            elif dir == 4:
                dir = 3

        if (mi, mj) not in new_D:       # 만약 새 딕셔너리에 이동한 좌표를 가진 key가 없다면
            new_D[(mi, mj)] = [Q, dir]  # 미생물 정보 추가
        else:                           # 만약 해당 좌표에 이미 미생물이 있다면 검사해야 한다고 need_check 딕셔너리에 기록해 둠
            if (mi, mj) not in need_check: # 처음 입력 받는 값은 이미 새 딕셔너리에 들어가 있던 값으로 할당해 주고
                need_check[(mi, mj)] = [new_D[(mi, mj)]]
            need_check[(mi, mj)].append([Q, dir])   # 이후에 추가함
        # print(need_check) # {(5, 7): [[634, 3], [416, 1], [712, 4]], (2, 3): [[796, 1], [549, 3]]}

    if need_check: # 만약 체크해야 하는 항목이 있다면
        for check_key, check_values in need_check.items(): # need_check 딕셔너리로부터 값을 받아와서
            ci, cj = check_key  # 좌표는 잠시 할당해주고
            check_values.sort(reverse=True) # 좌표들은 미생물 양이 많은 순으로 정렬해 줌
            M_dir = check_values[0][1]      # 방향은 미생물이 가장 많은 군집의 이동방향으로 설정됨

            Q_sum = 0   # 해당 좌표 값의 미생물들  합치기
            for check_value in check_values:
                Q_sum += check_value[0]
            new_D[(ci, cj)] = [Q_sum, M_dir] # 새 딕셔너리에 다 더해진 미생물의 수와, 방향 정보를 기록

    return new_D # 새 딕셔너리 반환

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) # N: 한 변 크기, M: 격리 시간, K: 군집 수

    # 1: 상, 2: 하, 3: 좌, 4: 우 (연산 편하게 하려고 0 앞에 추가함)
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    D = {} # 좌표, 미생물 세부 정보 담을 딕셔너리

    for _ in range(K): # 미생물 입력 받기 (좌표, 미생물 수, 방향)
        i, j, Q, dir = map(int, input().split())
        D[(i, j)] = [Q, dir]    # 해당 좌표 값을 key로, 양과 방향을 value로 해서 딕셔너리에 저장
                                # 최초에 동일한 좌표에 둘 이상의 미생물이 배치되는 경우는 없다해서, 따로 조건 추가 안 함

    for _ in range(M):  # 격리 시간만큼 move함수 호출
        D = move(D)     # 매 반복마다 반환되는 새 딕셔너리로 D 갱신

    # print(D) # {(1, 1): [3, 2], (0, 1): [3, 2], (5, 3): [5, 4], (2, 3): [25, 1], (1, 5): [108, 1], (3, 5): [1, 1]}

    result = 0
    for value in D.values(): # 최종 딕셔너리를 순회하며 미생물들의 양만 수집해 더함
        result += value[0]

    print(f'#{tc} {result}')

