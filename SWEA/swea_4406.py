o = ['a', 'e', 'i', 'o', 'u']

t = int(input())

for tt in range(t):
    l = input()

    for s in o:
        l = l.replace(s, '')
            
    print(f'#{tt + 1} {l}')
