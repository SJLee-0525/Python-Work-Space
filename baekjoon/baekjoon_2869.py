from math import *

a, b, v = map(int, input().split())

day_move = a - b
temp_v = v - a

temp_day = ceil(temp_v / day_move)
day = (temp_day + 1)

print(day)

# A, B, V = map(int, input().split())

# x = (V-B)/(A-B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)
