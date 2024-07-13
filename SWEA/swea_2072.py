from sys import *

t = int(stdin.readline())

for _ in range(t):
    n_list = list(map(int, stdin.readline().split()))
    s = 0
    for n in n_list:
        if n % 2 == 1:
            s += n
        else:
            continue
    print(f'#{_ + 1} {s}')