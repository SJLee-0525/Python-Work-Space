l = []

for i in range(100):
    l.append([0] * 100)

n = int(input())

for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            l[i][j] = 1

ls = sum(l, [])
print(ls.count(1))