T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # N 노드 개수, M 리프 노드 개수, L 출력할 노드 번호

    tree = [0] * (N + 1)    # 트리 생성

    for _ in range(M):      # 리프 노드 개수 만큼 반복
        i, num = map(int, input().split()) # 리프 노드 번호, 해당 번호가 갖는 값
        tree[i] = num                      # 해당 노드에 값 추가

    # print(tree) # [0, 0, 0, 0, 0, 0, 501, 170, 42, 468, 335]

    for ii in range(N - M, 0, -1):  # 리프 노드들을 제외한 곳들을 역순으로 탐색
        tree[ii] = tree[ii * 2]     # 리프 노드가 아니니 부모 요소에 왼쪽 자식 값은 추가 해주고
        if (ii * 2) + 1 <= N:       # 만약 오른쪽 자식이 존재한다면
            tree[ii] += tree[(ii * 2) + 1]  # 오른쪽 자식 값도 추가

    # print(tree) # [0, 1516, 845, 671, 510, 335, 501, 170, 42, 468, 335]
    print(f'#{tc} {tree[L]}')