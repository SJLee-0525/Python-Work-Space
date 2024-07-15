from sys import *

def binary_search(target, find_list):
    start = 0
    end = len(find_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_list[mid] == target:
            return 1
        elif find_list[mid] < target:
            start = end + 1
        else:
            end = mid - 1
    return 0

n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))
n_list.sort()

c = 0
for i in range(m):
    c += binary_search(i, n_list)
    print(c)

    


