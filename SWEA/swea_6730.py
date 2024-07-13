t = int(input())

for tt in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    cresc = []
    decresc = []
    for i in range(n - 1):
        if l[i] - l[i + 1] < 0:
            cresc.append(abs(l[i] - l[i + 1]))
        elif l[i] - l[i + 1] > 0:
            decresc.append(l[i] - l[i + 1])
        elif l[i] - l[i + 1] == 0:
            cresc.append(l[i] - l[i + 1])
            decresc.append(l[i] - l[i + 1])

    if len(cresc) == 0:
        cresc.append(0)
    if len(decresc) == 0:
        decresc.append(0)

    print(f'#{tt + 1} {max(cresc)} {max(decresc)}')
    