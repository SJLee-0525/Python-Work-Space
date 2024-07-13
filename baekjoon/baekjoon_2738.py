x, y, z = [], [], []

n, m = map(int, input().split())

# for i in range(n):
#     x.append(list(map(int, input().split())))

# for j in range(n):
#     y.append(list(map(int, input().split())))

# for k in range(n):
#     d = [(a + b) for a, b in zip(x[k], y[k])]
#     z.append(d)

# for h in z:
#     print(*h)

for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)

for i in range(n):
    b = list(map(int, input().split()))
    y.append(b)

for i in range(n):
    for j in range(m):
        result = x[i][j] + y[i][j]
        print(result, end = ' ')
    print()