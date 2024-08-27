import sys

# def move_split(arr, N):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0 and arr[i][j][3] >= 2:
#

def move(arr, N):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]  # 새 맵 생성

    B = True
    for i in range(N):
        for j in range(N):
            if arr[i][j]:      # 순회하다가 공이 있는 곳을 만나면
                temp_list = arr[i][j]
                for temp in temp_list:
                    ti = (i + (di[temp[2]] * temp[1])) % N # 이동한 값을 계산
                    tj = (j + (dj[temp[2]] * temp[1])) % N # temp[2] = d | temp[1] = s
                    if not new_arr[ti][tj]:     # 만약 새 맵에서 이동한 좌표가 비어있다면
                        new_arr[ti][tj].append(temp)  # 추가
                    else:                       # 비어있지 않다면 합치고
                        print(new_arr[ti][tj])
                        new_arr[ti][tj][0][0] += temp[0]
                        new_arr[ti][tj][0][1] += temp[1]
                        new_arr[ti][tj][0][2] += temp[2]
                        new_arr[ti][tj][0][3] += temp[3]
                        new_arr[ti][tj][0][4] += temp[4]
                        B = False

    if B == False:
        new_arr = ball_split(new_arr, N)
        print(new_arr)

    return new_arr

# temp[0] = m | temp[1] = s | temp[2] = d | temp[3] = 합쳐진 수 | temp[4] = 홀짝여부
def ball_split(arr, N):
    print('#', arr)
    new_arr = [[[] for _ in range(N)] for _ in range(N)]  # 새 맵 생성
    for i in range(N):
        for j in range(N):
            if arr[i][j]: # 만약 합쳐져서 값이 2 이상이라면
                temp_l = arr[i][j]
                if temp_l[0][3] >= 2:
                    temp = temp_l[0]
                    temp[0] = temp[0] // 5 # 질량
                    if temp[0] == []: # 질량이 0이되면 소멸되어 사라짐
                        break
                    temp[1] = temp[1] // temp[3] # 속력

                    if temp[4] % temp[3] == 0: # 합쳐진 방향이 모두 짝수거나 홀수면
                        for k in [0, 2, 4, 6]:
                            new_arr[i][j].append([temp[0], temp[1], k, 1, k % 2])
                        # for k in [0, 2, 4, 6]:
                            # new_arr[(i + di[k]) % N][(j + dj[k]) % N] = [temp[0], temp[1], k, 1, k % 2]
                    else:
                        for k2 in [1, 3, 5, 7]:
                            new_arr[i][j].append([temp[0], temp[1], k2, 1, k2 % 2])
                        # for k2 in [1, 3, 5, 7]:
                            # new_arr[(i + di[k2]) % N][(j + dj[k2]) % N] = [temp[0], temp[1], k2, 1, k2 % 2]
                    arr[i][j] = []
    # print('##', arr)
    print('###', new_arr)
    return new_arr



###############################################################################

N, M, K = map(int, sys.stdin.readline().split())
# N: 격자 크기, M: 볼 개수, K: 이동 명령 횟수

arr = [[[] for _ in range(N)] for _ in range(N)]  # 새 맵 생성

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# ball_list = []
for _ in range(M):
     r, c, m, s, d = map(int, sys.stdin.readline().split())
     r, c = r - 1, c - 1
     if d % 2 == 0: # 짝수면
         b = 0
     else:          # 홀수면
         b = 1
     # ball_list.append([r, c, m, s, d, 1])
     # 위치:(r, c), m: 질량, d: 방향, s: 속력
     arr[r][c].append([m, s, d, 1, b])

for _ in range(K):
    arr = move(arr, N)

print('Ans', arr)

