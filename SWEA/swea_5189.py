def perm(n, N):
    '''한 번씩만 방문해야 하니까 중복 순열 X'''
    if n == N - 1:        # 실제 N보다 한 번 덜 돌거임. 이유는 아래
        cal_usage(perm_list, N) # 완료되면 만들어진 순열로 계산 함수 호출
        return
    for i in range(1, N): # 시작점은 1(index 상으로는 0 고정)이니까, 0을 제외하고 순회
        if used[i]:       # 사용했으면 건너뜀
            continue
        perm_list.append(i) # permu 리스트에 담고
        used[i] = 1         # 사용 표시
        perm(n + 1, N)      # 순열 재귀 호출
        perm_list.pop()     # 사용했으면 다시 뽑고
        used[i] = 0         # 사용 표시 취소

def cal_usage(i_list, N):
    '''만들어진 순열로 전기 사용량 계산'''
    global result
    i_list = [0] + i_list + [0] # 시작점과 도착점은 무조건 0이니까 만들어진 함수에 합침
    temp = 0
    for i in range(N):          # 돌면서 점수표에 담음
        temp += E_V[i_list[i]][i_list[i + 1]]
    if result > temp:           # 최소값 할당
        result = temp

##################################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    E_V = [list(map(int, input().split())) for _ in range(N)]  # 전기 사용량 표

    perm_list = []  # 순열 담을 리스트
    used = [0] * N  # 사용 표시
    result = 100000

    perm(0, N)

    print(f'#{tc} {result}')