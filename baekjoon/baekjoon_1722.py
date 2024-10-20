import sys

def perm(lv):
    global cnt

    if lv == N:
        cnt += 1
        if prompt == 1:
            if cnt == num[0]:
                print(*path)
                return
        else:
            if num == path:
                print(cnt)
                return
        return

    for j in range(N):
        if used[j]:
            continue
        used[j] = 1
        path.append(arr[j])
        perm(lv + 1)
        used[j] = 0
        path.pop()

############################################################

N = int(sys.stdin.readline())
prompt, *num = map(int, sys.stdin.readline().split())

cnt = 0
arr = list(range(1, N + 1))
used = [0] * N
path = []

perm(0)