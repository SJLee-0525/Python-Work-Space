def find_set(i):
    '''i의 대표 원소 찾기'''
    while rep[i] != i:  # 대표 원소가 아니면 : 자기 자신을 가리키지 않으면 : index != 값값
       i = rep[i]      # i가 가리키는 원소가 대표인지 확인, 값을 새로운 인덱스
    return i

##########################################################################

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rep = list(range(N + 1))  # 대표 원소 make_set(1) ~ make_set(N)

    for i in range(M):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        rep[find_set(n1)] = find_set(n2)

    cnt = 0
    for i in range(1, N + 1):
        if rep[i] == i: # 자기 자신을 가리키는 경우
            cnt += 1

    print(f'#{tc} {cnt}')