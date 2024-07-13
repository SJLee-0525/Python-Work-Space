t = int(input())

for tt in range(t):
    n, m = map(int, input().split())

    l = []
    for _ in range(n):
        ll = list(map(int, input().split()))
        l.append(ll)

    t_l = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            
            temp = []
            for x in range(i, i + m):
                for y in range(j, j + m):
                    temp.append(l[x][y])
            
            s = sum(temp)
            t_l.append(s)

    print(f'#{tt + 1} {max(t_l)}')