def perm(i, N):
    '''연산자 리스트 받아서 순열 생성
    그냥 돌리니까 너무 느렸음..'''
    if i == N: # 연산자 순서 순열 완성되면 그걸 기반으로 계산 함수 돌림
        cal(oper_list)
        return
    else:
        seen = set() # 함수 레벨에서 세트를 사용해 중복된 값의 순열 생성을 방지
        for j in range(i, N):
            if oper_list[j] not in seen: # 중복된 값은 건너뜀
                seen.add(oper_list[j])   # seen 세트에 해당 요소 추가
                oper_list[i], oper_list[j] = oper_list[j], oper_list[i]
                perm(i + 1, N)
                oper_list[i], oper_list[j] = oper_list[j], oper_list[i]


def cal(i_oper_list):
    '''연산자 순서를 받아 계산 수행'''
    global max_v
    global min_v

    temp = num_list[0] # 첫번째 숫자 배정

    # 연산자를 받아서 명령에 맞는 연산 수행
    for i in range(len(i_oper_list)):
        if i_oper_list[i] == 0:
            temp = temp + num_list[i + 1]
        elif i_oper_list[i] == 1:
            temp = temp - num_list[i + 1]
        elif i_oper_list[i] == 2:
            temp = temp * num_list[i + 1]
        elif i_oper_list[i] == 3:
            temp = int(temp / num_list[i + 1])
            # 나눗셈의 경우 소숫점 버림

    # 최대, 최소값 조정
    if max_v < temp:
        max_v = temp
    if min_v > temp:
        min_v = temp

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 숫자 개수
    oper_cnt = list(map(int, input().split())) # 0: +, 1: -, 2: *, 3: /
    num_list = list(map(int, input().split()))

    # 연산자 개수별로 연산자 리스트 작성
    oper_list = []
    for o, c in enumerate(oper_cnt):
        for _ in range(c):
            oper_list.append(o)
    # print(oper_list) # [0, 0, 1, 3]

    max_v = -100000001
    min_v = 100000001

    perm(0, len(oper_list))

    print(f'#{tc} {max_v - min_v}')