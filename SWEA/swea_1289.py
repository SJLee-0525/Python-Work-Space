t = int(input())

for tt in range(t):
    ob_mem = list(map(int, input()))

    mem = []
    mem.append(ob_mem[0])
    for i in range(1, len(ob_mem)):
        if ob_mem[i] != mem[-1]:
            mem.append(ob_mem[i])

    if mem[0] == 0:
        print(f'#{tt + 1} {len(mem) - 1}')

    if mem[0] == 1:
        print(f'#{tt + 1} {len(mem)}')