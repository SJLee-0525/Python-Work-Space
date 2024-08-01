T = int(input())

for test_case in range(1, T + 1):
    find_target = input()
    test_target = input()

    find_target_len = 0
    for f_t in find_target:
        find_target_len += 1
    
    test_target_len = 0
    for t_t in test_target:
        test_target_len += 1
    
    judge = False
    for i in range(test_target_len - find_target_len + 1):
        if test_target[i:i + find_target_len] == find_target:
            print(f'#{test_case} 1')
            judge = True
            break
    if judge == False:
        print(f'#{test_case} 0')
