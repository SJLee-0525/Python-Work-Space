def order(node):
    global cnt
    if node == 0:   # 0이면 더 갈 데가 없으니 리턴
        return
    cnt += 1        # 있으면 카운트 올려주고 좌우 순서로 탐색
    order(left[node])
    order(right[node])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split()) # E 간선 수, N 시작점
    arr = list(map(int, input().split()))

    left = [0] * (E + 2) # 노드 수는 간선 수 + 1 (인덱스 고려해서 2를 더함)
    right = [0] * (E + 2)
    # par = [] # 시작점을 주기에 굳이 par 리스트 만들 필요 없을 듯

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        # par[c] = p

    # print(left, right)   # [0, 6, 1, 0, 0, 3, 4] [0, 0, 5, 0, 0, 0, 0]

    cnt = 0
    order(N)

    print(f'#{tc} {cnt}')