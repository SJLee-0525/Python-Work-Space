from sys import *

n, m = map(int, stdin.readline().split())

board = []
repair = []

for i in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        first_b = 0
        first_w = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] == "B":
                        first_w += 1
                    if board[k][l] == "W":
                        first_b += 1
                else:
                    if board[k][l] == "B":
                        first_b += 1
                    if board[k][l] == "W":
                        first_w += 1

        repair.append(first_w)
        repair.append(first_b)

print(repair)
print(min(repair))