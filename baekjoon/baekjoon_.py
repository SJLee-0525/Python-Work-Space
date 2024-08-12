'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

### 반례 ###
2
3 4
0
0
# 1

2
1 3
1 2
1 1
# 2

2
1 10
0
0
# 9

3
1 1 3
1 3
1 3
2 2 1
# 3

9
1 2 3 4 5 6 7 8 9
3 5 6 8
3 5 7 9
3 4 5 8
3 3 5 9
8 1 2 3 4 6 7 8 9
3 1 5 7
3 2 5 6
3 1 3 5
3 2 4 5
# 1
'''
def cut_dfs(s):
    visited[s] = 1
    # print(s, end=' ')
    pop_sum = pop_dict[s]
    stack = []
    while 1:
        for w in temp_adj_list[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w # 이동
                # print(s, end=' ')
                visited[s] = 1
                pop_sum += pop_dict[s]
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    # temp_sum_list.append(pop_sum)
    # print()
    return pop_sum

def dfs(s):
    visited[s] = 1
    # print(s, end=' ')
    pop_sum = pop_dict[s]
    stack = []
    while 1:
        for w in adj_list[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w # 이동
                # print(s, end=' ')
                visited[s] = 1
                pop_sum += pop_dict[s]
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    # temp_sum_list.append(pop_sum)
    # print()
    return pop_sum


import sys
# import copy
from itertools import combinations

N = int(sys.stdin.readline()) # 구역의 개수
pop_list = list(map(int, sys.stdin.readline().split())) # 구역별 인구 수 [5, 2, 3, 4, 1, 2]
pop_dict = {i + 1:pop_list[i] for i in range(N)} # 구역:인구수 딕셔너리 생성 {1: 5, 2: 2, 3: 3, 4: 4, 5: 1, 6: 2}
min_pop = 101

# 2차원 리스트를 활용해 각 노드의 연결 정보를 표현하기 
adj_list = [[] for _ in range(N + 1)]
for n in range(1, N + 1): # 
    many, *adj_cities = map(int, sys.stdin.readline().split())
    adj_list[n].extend(adj_cities)
# print(adj_list) # [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]

precise_route = set() # 중복 제거를 위해 set 사용
for u in range(1, N + 1): # 인접
    for v in adj_list[u]:
        if u < v:
            precise_route.add((u, v))
# print(precise_route) # {(1, 2), (3, 4), (1, 4), (2, 3), (2, 6), (2, 5)}

# 경로 만들기
# if adj_cities:
#     for a in adj_cities:
#         temp_a = list((n, a)) # 밑에서 정렬하기 위해서 리스트로 받음
#         temp_a.sort() # 중복 제거를 위해 정렬
#         temp_a = tuple(temp_a) # 튜플로 변환해 줘야 리스트 내에서 리스트 중복 제거가 가능한 듯
#         precise_route.append(temp_a)
# precise_route = list(set(precise_route)) # 중복 제거

    # for adj_city in adj_cities:
    #     adj_list[adj_city].append(n)

print(precise_route) # [(1, 2), (3, 4), (1, 4), (2, 3), (2, 6), (2, 5)]

# 경로에 대한 조합 생성
if not adj_cities and len(pop_dict) == 2:
    min_pop = abs(pop_list[0] - pop_list[1])

for x in range(1, len(precise_route) + 1):
    combi = list(combinations(precise_route, x))
    # print(combi) # [((1, 2),), ((3, 4),), ((1, 4),), ((2, 3),), ((2, 6),), ((2, 5),), ((1, 2), (3, 4)), ((1, 2), (1, 4)), ((1, 2), (2, 3)), ((1, 2), (2, 6)), ((1, 2), (2, 5)), ((3, 4), (1, 4)), ((3, 4), (2, 3)), ((3, 4), (2, 6)), ((3, 4), (2, 5)), ((1, 4), (2, 3)), ((1, 4), (2, 6)), ((1, 4), (2, 5)), ((2, 3), (2, 6)), ((2, 3), (2, 5)), ((2, 6), (2, 5)), ((1, 2), (3, 4), (1, 4)), ((1, 2), (3, 4), (2, 3)), ((1, 2), (3, 4), (2, 6)), ((1, 2), (3, 4), (2, 5)), ((1, 2), (1, 4), (2, 3)), ((1, 2), (1, 4), (2, 6)), ((1, 2), (1, 4), (2, 5)), ((1, 2), (2, 3), (2, 6)), ((1, 2), (2, 3), (2, 5)), ((1, 2), (2, 6), (2, 5)), ((3, 4), (1, 4), (2, 3)), ((3, 4), (1, 4), (2, 6)), ((3, 4), (1, 4), (2, 5)), ((3, 4), (2, 3), (2, 6)), ((3, 4), (2, 3), (2, 5)), ((3, 4), (2, 6), (2, 5)), ((1, 4), (2, 3), (2, 6)), ((1, 4), (2, 3), (2, 5)), ((1, 4), (2, 6), (2, 5)), ((2, 3), (2, 6), (2, 5)), ((1, 2), (3, 4), (1, 4), (2, 3)), ((1, 2), (3, 4), (1, 4), (2, 6)), ((1, 2), (3, 4), (1, 4), (2, 5)), ((1, 2), (3, 4), (2, 3), (2, 6)), ((1, 2), (3, 4), (2, 3), (2, 5)), ((1, 2), (3, 4), (2, 6), (2, 5)), ((1, 2), (1, 4), (2, 3), (2, 6)), ((1, 2), (1, 4), (2, 3), (2, 5)), ((1, 2), (1, 4), (2, 6), (2, 5)), ((1, 2), (2, 3), (2, 6), (2, 5)), ((3, 4), (1, 4), (2, 3), (2, 6)), ((3, 4), (1, 4), (2, 3), (2, 5)), ((3, 4), (1, 4), (2, 6), (2, 5)), ((3, 4), (2, 3), (2, 6), (2, 5)), ((1, 4), (2, 3), (2, 6), (2, 5)), ((1, 2), (3, 4), (1, 4), (2, 3), (2, 6)), ((1, 2), (3, 4), (1, 4), (2, 3), (2, 5)), ((1, 2), (3, 4), (1, 4), (2, 6), (2, 5)), ((1, 2), (3, 4), (2, 3), (2, 6), (2, 5)), ((1, 2), (1, 4), (2, 3), (2, 6), (2, 5)), ((3, 4), (1, 4), (2, 3), (2, 6), (2, 5)), ((1, 2), (3, 4), (1, 4), (2, 3), (2, 6), (2, 5))]
    # print(len(combi))
# 경로 조합들을 가져와서 하나씩 경로들을 끊어봄
    for mini_combi in combi: # 이전 코드에서는 조합을 다 불러와 리스트에 담았음. 아마 메모리 초과의 원인이었을 가능성이 큼. 
        # temp_adj_list = copy.deepcopy(adj_list) <- 메모리 초과의 원인일 수 있음
        temp_adj_list = [lst[:] for lst in adj_list] # gpt 추천, 이러면 깊은 복사 비스무리하게 되나?
        for mc in mini_combi:
            a, b = mc
            temp_adj_list[a].remove(b)
            temp_adj_list[b].remove(a)
            # 이번에는 조합을 뽑자마자 바로 돌림
            print('temp_adj', temp_adj_list)

# for city in range(1, N + 1):
#     temp_adj_list = copy.deepcopy(adj_list)
#     for adj in adj_list[city]:
#         temp_adj_list[adj].remove(city)
#     temp_adj_list[city].clear()

# 연결 끊기

# for city in range(1, N + 1):
#     temp_adj_list = copy.deepcopy(adj_list)
#     for adj in adj_list[city]:
#         temp_adj_list[adj].remove(city)
#     temp_adj_list[city].clear()
    # print(temp_adj_list)

    # 조합들로 경로를 지울 때마다 하나씩 다 돌아봄
        sum_list = []           # 끊어진 선거구의 인구수 합을 담을 리스트
        visited = [0] * (N + 1) # 방문 여부 확인
        for city_2 in range(1, N + 1):
            if sum(visited) == N:   # 다 방문했으면:
                # visited = [0] * (N + 1)
                break              # 돌지마
            if temp_adj_list[city_2] and visited[city_2] == 0: # 방문 안 한 경우에만 돌림
                sum_list.append(cut_dfs(city_2))
            # for city_3 in range(1, N + 1):
            elif not temp_adj_list[city_2] and visited[city_2] == 0: # 방문 안 한 경우에만 돌림
                sum_list.append(dfs(city_2)) 
                # 위 함수는 경로를 자른 것을 순회하는 함수가 아님. 
                # 경로들이 잘려있기 때문에, 위에서 쓴 함수로는 일부 나머지 부분을 순회할 수 없었음
                # visited는 공유하기 때문에, 중복되지는 않을 것 같음

        sum_list = list(set(sum_list)) # 중복 제거
    
        if len(sum_list) == 1 and sum(sum_list) != sum(pop_list): 
            # 만약 중복 제거 후 값이 하나라면 0으로 할당: 근데 만약 값이 원래 total 인구면 안 잘렸다는 소리니 그건 제외하고
            min_pop = 0
        elif len(sum_list) == 2:
            # 값이 2개면 선거구가 2개로 나눠졌다는 소리임, 둘의 차 계산
            # print(sum_list)
            temp_min_pop = abs(sum_list[0] - sum_list[1])
            if min_pop > temp_min_pop:
                min_pop = temp_min_pop

if min_pop == 101:
    # 바뀐 적이 없다면 불가능하다는 소리니, -1 출력
    print(-1)
else:    
    print(min_pop)