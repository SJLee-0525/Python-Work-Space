t = int(input())

for tt in range(t):
    a, b = map(int, input().split())

    count = 0
    for i in range(a, b + 1):
        i_2 = i ** 0.5
        if i_2 == int(i_2):
            i_2 = int(i_2)

        i = str(i)
        i_2 = str(i_2)

        if i == i[::-1]:
            if i_2 == i_2[::-1]:
                count += 1

    print(f'#{tt + 1} {count}')
