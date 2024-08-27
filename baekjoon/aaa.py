import sys

def move(D):
    B = True
    new_D = {}
    # print('DDD', D)
    for k, v in D.items():
        if D[k] == []:
            continue
        else:
            for mv in v:
                # print(D)
                # print(k)
                # print(mv)
                ti = (k[0] + (di[mv[2]] * mv[1])) % N
                tj = (k[1] + (dj[mv[2]] * mv[1])) % N

                if (ti, tj) not in new_D:
                    new_D[(ti, tj)] = [mv]
                    # print('n', new_D)
                else:
                    B = False
                    # W = True
                    for kk in range(5):
                        # print(new_D[(ti, tj)])
                        new_D[(ti, tj)][0][kk] += mv[kk]
                        

    if B == True:
        return new_D
    else:
        return ball_split(new_D)

def ball_split(D):
    new_D = {}
    for k, vv in D.items():
        if D[k] == []:
            continue
        else:
            for v in vv:
                if v[3] >= 2:
                    temp = []
                    m = v[0] // 5
                    s = v[1] // v[3]
                    if v[4] % v[3] == 0 and m != 0: 
                    # 합쳐진 방향이 모두 짝수거나 홀수면 
                        for j in [0, 2, 4, 6]:
                            temp.append([m, s, j, 1, j % 2])
                    elif v[4] % v[3] == 1 and m != 0:
                        for j2 in [1, 3, 5, 7]:
                            temp.append([m, s, j2, 1, j2 % 2])
                    new_D[k] = temp
                else:
                    new_D[k] = D[k]

    # print('in', D)
    return new_D

# temp[0] = m | temp[1] = s | temp[2] = d | temp[3] = 합쳐진 수 | temp[4] = 홀짝여부

###################################################################

N, M, K = map(int, sys.stdin.readline().split())
# N: 격자 크기, M: 볼 개수, K: 이동 명령 횟수

D = {}

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
     D[(r, c)] = []
     D[(r, c)].append([m, s, d, 1, b])

# print(D)
for _ in range(K):
    D = move(D)
    # print(D)

# 마지막 정리?
new_D = {}
for k, v in D.items():
    if not D[k]:
        continue
    else:
        new_D[k] = v

# print(new_D)

cnt = 0
for key, value in new_D.items():
    if new_D[key]:
        for v in value:
            cnt += v[0]

print(cnt)
# for _ in range(K):
#     arr = move(arr, N)

# print('Ans', arr)