p, k = map(int, input().split())
c = 0

while 1:
    c += 1
    if p == k:
        break
    k += 1

print(c)
