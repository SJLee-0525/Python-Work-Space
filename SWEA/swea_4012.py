def cal_taste(food_type):
    global ingredients
    taste_sum = 0
    # 중복 없게끔 반복
    for f_num_1 in range(len(food_type)):
        for f_num_2 in range(f_num_1, len(food_type)):
            # 시너지 계산
            taste_sum += ingredients[food_type[f_num_1]][food_type[f_num_2]]
            taste_sum += ingredients[food_type[f_num_2]][food_type[f_num_1]]
    return taste_sum

def perm(i, N): # 순열로도 가능하지만 댕느림;
    global score_list
    if i == N // 2: # 중복 줄이기
        type_A = arr[:N//2]
        type_B = arr[N//2:]
        taste_score = abs(cal_taste(type_A) - cal_taste(type_B))
        score_list.append(taste_score)
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            perm(i + 1, N)
            arr[i], arr[j] = arr[j], arr[i]

def combi(i, N): # 조합으로 해보자
    global b
    global arr
    global score_list
    if i == N:
        if sum(b) == N//2: # 만약 b에서 True가 절반이라면
            type_A = []
            type_B = []
            for j in range(N):
                if b[j]: # 1이면 type_A에 담고
                    type_A.append(arr[j])
                else:   # 0이면 type_B에
                    type_B.append(arr[j])
            print(type_A, type_B)
            taste_score = abs(cal_taste(type_A) - cal_taste(type_B))
            score_list.append(taste_score)
    else:
        b[i] = 0
        combi(i + 1, N)
        b[i] = 1
        combi(i + 1, N)

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 식재료 수
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    score_list = []

    # perm(0, N)
    # print(score_list)

    b = [0] * N
    combi(0, N)

    print(f'#{tc} {min(score_list)}')