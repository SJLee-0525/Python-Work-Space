from sys import *
from math import *

# n = int(stdin.readline())

# for i in range(n):
#     a, b = map(int, stdin.readline().split())

#     print(lcm(a, b))
''' ---------------------------------------------------'''
n = int(input())

for i in range(n):
    a, b = map(int, stdin.readline().split())
    aa, bb = a, b

    while a % b != 0:
        a, b = b, a % b
 
    print(aa * bb // b)



# n = int(input())

# for _ in range(n):
#     x = list(map(int, input().split()))
#     a, b = x[0], x[1]
#     if a > b:
#         a, b = b, a

#     s_l = []
#     for i in range(2, max(x) + 1):
#         if a % i == 0 or b % i == 0:
#             s_l.append(i)
    
#     l = []
#     l2 = []
#     for j in s_l:
#         if a % j == 0:
#             while a % j == 0:
#                 l.append(j)
#                 a /= j

#     for j2 in s_l:
#         if b % j2 == 0:
#             while b % j2 == 0:
#                 l2.append(j2)
#                 b /= j2

#     for k in l:
#         if k not in l2:
#             l2.append(k)

#     result = 1
#     for f in l2:
#         result *= f

#     print(result)

        

    