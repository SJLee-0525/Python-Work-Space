T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 배열의 길이
    arr = list(map(int, input().split()))

    # 선택 정렬 과정
    for i in range(N - 1):
        # i의 범위는 전체 길이에서 하나를 뺌.
        # 최대값, 최소값 index는 반복 시작 시  i로 설정
        max_index = i
        min_index = i
        # 최소값보다 j번째 요소가 작거나, 최대값보다 j번째 요소가 크면 index 바꿔줌
        for j in range(i + 1, N):
            if arr[max_index] < arr[j]:
                max_index = j
            if arr[min_index] > arr[j]:
                min_index = j
        # 짝수번째에는 큰 값을, 홀수번째에는 작은값을 정렬하도록
        if i % 2 == 0:
            arr[i], arr[max_index] = arr[max_index], arr[i]
        else:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'#{test_case}', end=' ')
    for elem in arr[:10]:
        print(elem, end= ' ')
    print()