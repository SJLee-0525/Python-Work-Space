T = int(input())
for test in range(1, T + 1):
    # N은 정수의 개수, M은 구간의 길이
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    temp_i = M // 2

    result_list = []
    for index in range(N - M + 1):
        count = 0
        for i in range(index, index + M):
            count += arr[i]
        result_list.append(count)

    max_value = result_list[0]
    min_value = result_list[0]
    for value in result_list:
        if min_value > value:
            min_value = value
        elif max_value < value:
            max_value = value

    result = max_value - min_value
    print(f'#{test} {result}')
