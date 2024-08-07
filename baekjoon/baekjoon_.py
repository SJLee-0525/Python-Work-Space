import sys

C = int(sys.stdin.readline())

stair = [0] + [int(sys.stdin.readline()) for _ in range(C)]

i = 0
score = 0
while i <= C - 2:
    if stair[i + 1] >= stair[i + 2]:
        score += stair[i + 1]
        i += 1
    elif stair[i + 1] < stair[i + 2]:
        score += stair[i + 2]
        i += 2

if i == C - 1:
    score += stair[i + 1]

print(score)