T = int(input())

for test_case in range(1, T + 1):

    # str 요소 각각 list에 담기
    target_list = list(input())
    test_list = list(input())
    
    max_count = 0
    # 각각의 타겟들로 테스트 str을 검사
    for target in target_list:
        count = 0
        for test_s in test_list:
            if target == test_s:
                count += 1
        if max_count < count:
            max_count = count
    
    print(f'#{test_case} {max_count}')