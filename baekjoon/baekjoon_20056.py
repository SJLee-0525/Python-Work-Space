import sys

def move(D):
    '''움직임 수행 함수'''
    split_need = False      # 합쳐진 것이 있는지 확인용
    new_D = {}              # 새 딕셔너리를 만들어 데이터를 새로 삽입할 것임

    for k, v in D.items(): # 입력받은 딕셔너리를 순회
        if not v:    # 만약 해당 데이터가 없으면 (D[k] == [])
            continue # 넘김 (새 딕셔너리에 굳이 값 삽입하지 않음)
        elif v:      # 만약 데이터가 있다면
            for mv in v: # 해당 데이터를 순회 (v가 2차원 리스트 형태의 자료이기 때문)
                ti = (k[0] + (di[mv[2]] * mv[1])) % N
                tj = (k[1] + (dj[mv[2]] * mv[1])) % N
                # 위치 데이터와 방향, 속력 정보를 이용해서 이동할 곳의 좌표 계산

                if (ti, tj) not in new_D:   # 만약 해당 좌표 값이 새 딕셔너리에 없다면
                    new_D[(ti, tj)] = [mv]  # 값 추가 (2차원 리스트 형태로)
                else:                       # 만약 이미 해당 좌표 값이 새 딕셔너리에 있다면
                    split_need = True       # 합쳐졌으니, 분할 작업 수행해야 한다 표시
                    for kk in range(5):     # 순회하면서 값을 각자 합쳐줌
                        new_D[(ti, tj)][0][kk] += mv[kk]

    if split_need == True:       # 분할 작업이 필요하면
        return ball_split(new_D) # 분할 함수 호출하고 얻어지는 새 딕셔너리 반환
    else:                        # 필요 없으면 새 딕셔너리 반환
        return new_D


def ball_split(D):
    '''분할 수행 함수'''
    new_D = {}              # 새 딕셔너리를 만들어 데이터를 새로 삽입할 거임
    for k, vv in D.items(): # 입력받은 기존 딕셔너리르 순회
        if not D[k]:        # 만약 해당 데이터가 없으면 (D[k] == [])
            continue        # 넘김 (새 딕셔너리에 굳이 값 삽입하지 않음)
        else:               # 만약 데이터 값이 있다면
            temp = []       # << temp 위치 아래가 아니라 여기임
            for v in vv:        # 해당 데이터를 순회
                # print('vv', vv)
                if v[3] >= 2:       # v[3]의 값 == 합쳐진 개수
                    m = v[0] // 5   # 질량 새로 계산 (합쳐진 질량의 합 // 5)
                    if m == 0:      # 0이면 어차피 소멸되므로 넘김
                        continue
                    s = v[1] // v[3] # 속력 계산 (합쳐진 속력의 합 / 합쳐진 수)
                    if v[4] == 0 or v[4] == v[3]:
                        # 합쳐진 방향이 모두 짝수거나 홀수면:
                        # 전부 짝수라면 해당 데이터가 0일거고, 전부 홀수라면 합쳐진 수와 같을 거임
                        for j in [0, 2, 4, 6]: # 짝수 방향 설정해서 4개의 데이터 temp에 추가
                            temp.append([m, s, j, 1, 0])
                    else:   # 합쳐진 방향이 전부 짝수나 홀수가 아니라면..
                        for j2 in [1, 3, 5, 7]: # 홀수 방향 설정해서 4개의 데이터 temp에 추가
                            temp.append([m, s, j2, 1, 1])
                    new_D[k] = temp # 해당 좌표 값에 분할된 데이터 추가
                else:               # 합쳐지지 않았다면 (v[3] == 1)
                    new_D[k] = D[k] # 그냥 추가

    return new_D # 새롭게 생성한 딕셔너리 반환

# temp[0] = m | temp[1] = s | temp[2] = d | temp[3] = 합쳐진 수 | temp[4] = 홀짝여부
###################################################################

N, M, K = map(int, sys.stdin.readline().split())
# N: 격자 크기, M: 볼 개수, K: 이동 명령 횟수

D = {}  # 위치를 key로, 데이터를 value로 하는 딕셔너리 생성

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# ball_list = []
for _ in range(M):
    # 위치:(r, c), m: 질량, d: 방향, s: 속력
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1     #
    if d % 2 == 0:          # 짝수면 0
        b = 0
    else:                   # 홀수면 1
        b = 1

    D[(r, c)] = []
    D[(r, c)].append([m, s, d, 1, b])
    # 위치:(r, c), m: 질량, d: 방향, s: 속력, 1: 합쳐진 수, b: 홀짝 여부 판단용

for _ in range(K): # K번 동안 move 수행
    D = move(D)    # 매 반복마다 반환되는 새 딕셔너리를 재할당
    # print(D)

# 다 완성되면 딕셔너리를 순회
cnt = 0
for key, value in D.items():
    if D[key]: # 만약 데이터가 있다면
        for v in value: # 데이터를 순회하고
            cnt += v[0] # 질량값만을 추가

# 총 질량 출력
print(cnt)
