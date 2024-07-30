T = int(input())

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    # P = 페이지 수, A, B = 각자 찾아야 하는 수

    A_start, A_end = 1, P
    A_count = 1
    while A_start <= A_end:
        A_mid = (A_start + A_end) // 2
        if A == A_mid:
            break
        elif A < A_mid:
            A_end = A_mid 
            A_count += 1
        elif A > A_mid:
            A_start = A_mid 
            A_count += 1

    B_start, B_end = 1, P
    B_count = 1
    while B_start <= B_end:
        B_mid = (B_start + B_end) // 2
        if B == B_mid:
            break
        elif B < B_mid:
            B_end = B_mid 
            B_count += 1
        elif B > B_mid:
            B_start = B_mid
            B_count += 1        
    
    # print(A_count, B_count)
    if A_count == B_count:
        print(f'#{test_case} 0')
    elif A_count > B_count:
        print(f'#{test_case} B')
    elif A_count < B_count:
        print(f'#{test_case} A')
        