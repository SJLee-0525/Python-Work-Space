import heapq

def find_set(x):
    if parents[x] == x: # 부모가 자기 자신이면: 자기가 그 그룹의 대표자이므로
        return x        # 대표자 반환

    parents[x] = find_set(parents[x]) # 아니면 부모를 타고 올라가면서 경로 압축 (재귀)
    return parents[x]


def union(x, y):
    # 각 요소의 부모 요소를 꺼내옴
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y: # 이미 같은 부모를 가진 같은 집합이면 끝
        return
    if root_x > root_y:  # 다른 집합이라면: 더 작은 루트노드에 합치는 식으로 둘을 합침
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x

##################################################################################

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split()) # 마지막 노드 번호 V / 간선 개수 E

    route = []
    for _ in range(E):
        s, e, w = map(int, input().split()) # 출발, 도착, 가중치
        route.append([s, e, w])             # 위 정보를 묶어서 route 리스트에 저장

    route.sort(key=lambda x:x[2])           # 가중치를 기준으로 정렬
    parents = list(range(V + 1))            # 각 원소의 부모를 자기 자신으로 설정해 초기설정

    cnt = 0 # 선택한 route의 수 세는 변수 : 시간 효율을 위해, cnt == V가 되는 순간 중단할 용도
    rst = 0 # 가중치의 합을 저장할 변수
    for start, end, weight in route:
        if find_set(start) != find_set(end): # 둘이 같은 집합이 아니라면
            union(start, end)                # 합침
            cnt += 1                         # 카운트 증가해 주고
            rst += weight                    # 가중치 더해줌
            if cnt == V:                     # MST 구성이 끝나면
                break                        # 중단

    print(f'#{tc} {rst}')