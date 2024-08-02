T = int(input())

for test_case in range(1, T + 1):
    target_list = list(input())
    test_str = input()

    # 카운트 지정하고, 타겟들을 하나씩 뺴옴
    max_count = 0
    for target in target_list:
        # 문자열을 돌면서 각 요소들에 대해 카운트를 셈
        c = 0
        for test_s in test_str:
            if target == test_s:
                c += 1
        # 만약 max값이 현재값보다 작으면 바꿈
        if max_count < c:
            max_count = c

    print(f'#{test_case} {max_count}')
