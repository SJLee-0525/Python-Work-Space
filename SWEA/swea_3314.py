t = int(input())

for tt in range(t):
    l = list(map(int, input().split()))
    
    for i in range(len(l)):
        if l[i] < 40:
            l[i] = 40
    
    print(f'#{tt + 1} {int(sum(l)/len(l))}')
