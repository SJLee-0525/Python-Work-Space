t = int(input())

for tt in range(t):
    m1, d1, m2, d2 = map(int, input().split())

    c_d = 0
    if m1 != m2:
        for m in range(m1 + 1, m2):
            if m in [1, 3, 5, 7, 8, 10, 12]:
                c_d += 31
            elif m in [4, 6, 9, 11]:
                c_d += 30
            elif m == 2:
                c_d += 28
        
        if m1 in [1, 3, 5, 7, 8, 10, 12]:
            c_d += 32 - d1 + d2
        elif m1 in [4, 6, 9, 11]:
            c_d += 31 - d1 + d2
        elif m1 == 2:
            c_d += 29 - d1 + d2

    elif m1 == m2:
        c_d += d2 - d1 + 1

    print(f'#{tt + 1} {c_d}')
