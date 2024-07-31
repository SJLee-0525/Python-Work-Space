T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1):
        max_arr, min_arr = arr[i], arr[i]
        max_i, min_i = 0, 0
        for j in range(i, N):
            if max_arr < arr[j]:
                max_arr = arr[j]
                max_i = j
            if min_arr > arr[j]:
                min_arr = arr[j]
                min_i = j

        if i % 2 == 0:
            if arr[i] < max_arr:
                arr[i], arr[max_i] = arr[max_i], arr[i]
        elif i % 2 != 0:
            if arr[i] > min_arr:
                arr[i], arr[min_i] = arr[min_i], arr[i]

    print(f'#{test_case}', end = ' ')
    for elem in arr[:10]:
        print(elem, end = ' ')
    print()