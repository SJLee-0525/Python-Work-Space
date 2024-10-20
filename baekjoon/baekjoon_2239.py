import sys

def fillin(lv):
    global solved

    if solved:
        return

    if lv == len(empty_list):
        solved = True
        for j in range(9):
            temp = map(str, arr[j])
            print(''.join(temp))
        return

    ni, nj = empty_list[lv]
    impossible_nums = check(ni, nj)

    for num in range(1, 10):
        if not impossible_nums[num]:
            arr[ni][nj] = num
            fillin(lv + 1)
            arr[ni][nj] = 0

def check(i, j):
    impossible_nums = [0] * 10

    si, sj = i - i % 3, j - j % 3
    for ci in range(si, si + 3):
        for cj in range(sj, sj + 3):
            if arr[ci][cj]:
                impossible_nums[arr[ci][cj]] = 1

    for c in range(9):
        if arr[i][c]:
            impossible_nums[arr[i][c]] = 1
        if arr[c][j]:
            impossible_nums[arr[c][j]] = 1

    return impossible_nums

def check_empty():
    empty_list = []
    for i in range(9):
        for j in range(9):
            if not arr[i][j]:
                empty_list.append((i, j))

    return empty_list

########################################################################

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]

empty_list = check_empty()

solved = False
fillin(0)