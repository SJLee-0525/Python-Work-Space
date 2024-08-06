import sys

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())
    square_1 = [(x1, q1), (p1, q1), (p1, y1), (x1, y1)] # 1 2
    square_2 = [(x2, q2), (p2, q2), (p2, y2), (x2, y2)] # 4 3

    if x1 in range(x2, p2 + 1) or p1 in range(x2, p2 + 1) or y1 in range(y2, q2 + 1) or q1 in range(y2, q2 + 1):
        if (x1 == q2 and (y2 in range(y1, q2 + 1) or q2 in range(y1, q2 + 1))) or (q1 == x2 and
