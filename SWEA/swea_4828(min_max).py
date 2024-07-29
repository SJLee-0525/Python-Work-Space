# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라.

# 첫 줄에 테스트 케이스의 수 T가 주어진다
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다
# 다음 줄에 N개의 양수 ai가 주어진다.

T = int(input())
for test_num in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 배열 내에서 가장 큰 값과 작은 값 찾기
    num_max = arr[0]  # 배열의 가장 첫번째 값으로 초기값 할당하는 것 추천
    num_min = arr[0]

    # 배열을 돌면서 할당된 값과 비교
    for num in arr:
        if num_min > num:
            num_min = num
        elif num_max < num:
            num_max = num

    print(f'#{test_num} {num_max - num_min}')
