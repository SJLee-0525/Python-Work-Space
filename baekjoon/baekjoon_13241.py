from sys import *
# from math import *

# a, b = map(int, input().split())

# print(lcm(a, b))

a, b = map(int, input().split())
aa, bb = a, b

while aa % bb != 0:
    aa, bb = bb, aa % bb

print(a * b // bb)
