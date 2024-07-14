from sys import *

n = int(stdin.readline())

l = []
for _ in range(n):
    l.append(int(stdin.readline()))

l.sort()

b = []
for i in range(1, n):
    if l[i] == l[i - 1]:

print(int(sum(l)/n))
print(l[(n - 1) / 2])
print()
print(max(l) - min(l))