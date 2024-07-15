from sys import *

n = int(stdin.readline())
n_list = list(range(1, n + 1))
target = []
try_list = []

for _ in range(n):
    target.append(int(stdin.readline().strip()))

for i in target:
    for x in n_list:
        if x != i:
            if x < i:
                try_list.append()
