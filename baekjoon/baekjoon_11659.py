import sys

N, M = map(int, sys.stdin.readline().split())

index_list = list(range(1, N + 1)) # [1, 2, 3, 4, 5]
value_list = list(map(int, sys.stdin.readline().split())) # [5, 4, 3, 2, 1]

i_v_dict = dict(zip(index_list, value_list))
# 두 리스트를 묶어서 딕셔너리 생성 {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    result = 0
    for key in range(start, end + 1):
        result += i_v_dict[key]
    
    print(result)