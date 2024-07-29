T = int(input())

for test in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    init_result = 0
    for init in range(M):
        init_result += arr[init]
    max_result = init_result
    min_result = init_result

    for i in range(len(arr) - M + 1):
        temp_result = 0

        for j in range(i, i + M):
            temp_result += arr[j]
        if max_result < temp_result:
            max_result = temp_result
        elif min_result > temp_result:
            min_result = temp_result
        
    print(f'#{test} {max_result - min_result}')