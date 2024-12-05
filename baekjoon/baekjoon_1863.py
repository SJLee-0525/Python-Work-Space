import sys

N = int(sys.stdin.readline())

cnt = 0
stack = []
for _ in range(N):
    # print(stack, cnt)
    x, y = map(int, sys.stdin.readline().split())

    if not stack or stack[-1] < y:
        if y != 0:  # 0이 아닌 경우에만 넣자. 이거 안 넣어서 틀림. (마지막 stack에서 뽑으면서 오류나는 듯)
            stack.append(y)
    else:
        while stack and stack[-1] > y:
            stack.pop()
            cnt += 1
        if y != 0 and (not stack or stack[-1] != y):
            stack.append(y)

while stack:
    stack.pop()
    cnt += 1

print(cnt)