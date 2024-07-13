t = int(input())

for tt in range(t):
    f = 0
    l = []
    for _ in range(9):
        ll = list(map(int, input().split()))
        l.append(ll)

    for i in range(9):
        if sum(l[i]) != 45:
            f += 1
    
    t_l = [0] * 9
    for i in range(9):
        for j in range(9):
            t_l[j] = l[j][i]
        
        if sum(t_l) != 45:
            f += 1
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:

            temp = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    temp.append(l[x][y])

            if sum(temp) != 45:
                f += 1

    if f == 0:
        print(f'#{tt + 1} 1')
    elif f != 0:
        print(f'#{tt + 1} 0')