t = int(input())

for _ in range(t):
    num = int(input())

    test_l = list(map(int, input().split()))
    test_d = list(set(test_l))

    f_l = []
    for i in test_d:
        f_l.append(test_l.count(i))

    f = max(f_l)
    f_i = f_l.index(f)
    
    print(f'#{num} {test_d[f_i]}')