t = int(input())

for tt in range(t):
    ah, am, bh, bm = map(int, input().split())

    if am + bm < 60:
        m = am + bm

        if ah + bh <= 12:
            h = ah + bh
        elif ah + bh > 12:
            h = ah + bh - 12

    elif am + bm >= 60:
        m = am + bm - 60

        if ah + bh <= 12:
            h = ah + bh + 1
        elif ah + bh > 12:
            h = ah + bh - 11

    print(f'#{tt + 1} {h} {m}')