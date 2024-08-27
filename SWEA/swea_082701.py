def in_order(node):
    if node == 0:
        return
    in_order(LR[0][node])
    print(D[node], end='') # 해당 문자열 출력
    in_order(LR[1][node])

##################################################################################

for tc in range(1, 11):
    N = int(input()) # 정점 수

    D = {}                                  # 각 정점이 가지고 있는 문자열 정보
    LR = [[0] * (N + 1) for _ in range(2)]  # 좌우를 하나의 2차원 리스트로 관리
    par = [0] * (N + 1)                     # 부모 정보

    for _ in range(N):
        node, node_v, *adjL = input().split() # 노드 번호, 노드가 가진 문자열, *인접한 노드 정보
        node = int(node)    # 숫자로 바꾸고
        D[node] = node_v    # 딕셔너리에 번호를 key로 문자열을 value로 해서 저장
        if adjL:            # 만약 인접한 노드 정보가 있다면
            adjL = list(map(int, adjL))     # 리스트 통째로 int로 바꾸고
            for i, n_v in enumerate(adjL):  # 앞에있는 것은 LR[0]: left / 뒤의 요소는 LR[1]: Right
                LR[i][node] = n_v           # 맞춰서 저장
                par[n_v] = node             # 부모요소도 저장

    # print(LR) # [[0, 2, 4, 6, 8, 0, 0, 0, 0], [0, 3, 5, 7, 0, 0, 0, 0, 0]]
    # print(par) # [0, 0, 1, 1, 2, 2, 3, 3, 4]

    r = N               # 출발 노드 찾기
    while par[r] != 0:  # 0이 아닌동안 계속 돌기
        r = par[r]
    root = r            # 만약 부모 요소가 없어서 0인 애가 튀어나오면 걔가 루트

    print(f'#{tc}', end=' ')
    in_order(root)
    print()