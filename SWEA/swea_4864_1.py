T = int(input())

for test_case in range(1, T + 1):
    target = input()
    test = input()

    # 검사 값의 길이 구하기
    target_len = 0
    for elem in target:
        target_len += 1

    # 검사 대상의 길이 구하기
    test_len = 0
    for elem in test:
        test_len += 1

    # 판단할 요소 지정
    judge = False

    # 검사할 때 인덱스가 넘어가지 않게끔
    for i in range(test_len - target_len + 1):
        print(test[i:i+target_len])
        if target == test[i:i + target_len]:
            judge = True

    if judge == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
