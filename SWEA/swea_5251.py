import heapq

def dijkstra(start):
    H = []                          # 힙 생성
    heapq.heappush(H, (0, start))   # 힙 내부 정렬은 맨 앞 데이터를 기준으로 정렬하니
    distance[start] = 0             # 시작 노드 최단 거리는 0

    while H:
        dis, now = heapq.heappop(H) # 가장 최단 거리인 노드에 대한 정보 꺼내기
        if distance[now] < dis:     # 현재 노드가 이미 처리 됐다면 skip
            continue

        for nxt in graph[now]:      # 현재 노드와 인접한 노드 확인
            nxt_node = nxt[0]       # graph 내부에 삽입된 end 값
            cost = nxt[1]           # graph 내부에 삽입된 dis 값

            new_cost = dis + cost   # 현재 뽑아온 최단거리 dis 값에 방금 그래프에서 가져온 dis값을 합쳐 새 누적 거리 생성
            if new_cost >= distance[nxt_node]: # 그 노드를 가는 데에 더 많은 거리가 필요하면 스킵
                continue

            distance[nxt_node] = new_cost       # 여기까지 오면 최소거리임. 해당 노드 값에 할당
            heapq.heappush(H, (new_cost, nxt_node)) # 힙에 넣어서 다음 연산 할 수 있게금

##########################################################################

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split()) # 마지막 연결지점 번호 / 도로 개수
    graph = [[] for _ in range(N + 1)]
    distance = [100000001] * (N + 1)

    for _ in range(E):
        st, end, dis = map(int, input().split())
        graph[st].append([end, dis])

    dijkstra(0)

    print(f'#{tc} {distance[N]}')