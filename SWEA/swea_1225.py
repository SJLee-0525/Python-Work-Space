for _ in range(10):
    t = int(input())
    l = list(map(int, input().split()))
    l_2 = [1, 2, 3, 4, 5]

    while 1:
        for i_2 in l_2:
            temp = l.pop(0) - i_2
            if temp <= 0:
                l.append(0)
                break
            l.append(temp)
        if l[-1] == 0:
            break
            

    print(f'#{t}', end = ' ')
    print(*l)