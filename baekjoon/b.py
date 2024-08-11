import sys
import copy
from itertools import combinations

N = int(sys.stdin.readline()) # 구역의 개수
pop_list = list(map(int, sys.stdin.readline().split())) # 구역별 인구 수 [5, 2, 3, 4, 1, 2]
pop_dict = {i + 1: pop_list[i] for i in range(N)} # 구역: 인구수 딕셔너리 생성
min_pop = float('inf')  # 초기값을 무한대로 설정

# 2차원 리스트를 활용해 각 노드의 연결 정보를 표현하기
adj_list = [[] for _ in range(N + 1)]
for n in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().split()))
    many = data[0]
    adj_list[n] = data[1:]

# 그래프의 간선 리스트를 만들고 중복 제거
edges = set()
for u in range(1, N + 1):
    for v in adj_list[u]:
        if u < v:
            edges.add((u, v))

# 그래프의 모든 간선 조합을 생성
combi = []
for x in range(1, len(edges) + 1):
    combi.extend(combinations(edges, x))

def cut_and_check(subset):
    temp_adj_list = copy.deepcopy(adj_list)
    for u, v in subset:
        temp_adj_list[u].remove(v)
        temp_adj_list[v].remove(u)

    visited = [False] * (N + 1)
    sum_list = []

    def dfs(start):
        stack = [start]
        visited[start] = True
        component_sum = pop_dict[start]
        while stack:
            node = stack.pop()
            for neighbor in temp_adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    component_sum += pop_dict[neighbor]
                    stack.append(neighbor)
        return component_sum

    for i in range(1, N + 1):
        if not visited[i] and temp_adj_list[i]:
            sum_list.append(dfs(i))

    if len(sum_list) == 2 and sum(sum_list) == sum(pop_list):
        return abs(sum_list[0] - sum_list[1])
    return float('inf')

for edge_combination in combi:
    min_pop = min(min_pop, cut_and_check(edge_combination))

if min_pop == float('inf'):
    print(-1)
else:
    print(min_pop)
