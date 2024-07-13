t = int(input())

for tt in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    average = sum(l) / n
    c = 0

    for i in l:
        if i <= average:
            c += 1

    print(f'#{tt + 1} {c}')