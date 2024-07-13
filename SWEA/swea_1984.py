t = int(input())

for tt in range(t):
    l = list(map(int, input().split()))

    l.remove(max(l))
    l.remove(min(l))

    print(f'#{tt + 1} {round(sum(l)/len(l))}')