import sys

k, n = tuple(map(int, sys.stdin.readline().split()))

lan_cables = []
for _ in range(k):
    lan_cables.append(int(sys.stdin.readline()))

lan_cables.sort()

cut_len = lan_cables[0]

while 1:    
    try:
        cut_count = 0
        for lan_cable in lan_cables:
            cut_count += (lan_cable // cut_len)
        if cut_count < n:
            cut_len //= 2
            cut_count = 0
        elif cut_count > n:
            cut_len = int(cut_len * 1.75)
            cut_count = 0 
        elif cut_count == n:
            break
    except:
        continue

while 1:
    cut_count = 0
    for lan_cable in lan_cables:
        cut_count += (lan_cable // cut_len)
    if cut_count < n:
        break
    cut_len += 1

print(cut_len - 1)


