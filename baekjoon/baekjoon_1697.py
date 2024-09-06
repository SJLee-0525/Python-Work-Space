import sys

def find_D(S, i_D, c):
    global count
    if i_D == S:
        if count > c:
            count = c
        return
    if c >= count:
        return
    if S > i_D:
        find_D(S, i_D + 1, c + 1)
    else:
        find_D(S, i_D + 1, c + 1)
        find_D(S, i_D - 1, c + 1)
        find_D(S, i_D // 2, c + 1)


###################################################

S, D = map(int, sys.stdin.readline().split())
count = 1000000
find_D(S, D, 0)
print(count)
