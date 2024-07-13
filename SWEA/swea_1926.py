n = int(input())

l = ['3', '6', '9']
for i in range(1, n + 1):
    s = list(str(i))

    b = 0
    for ss in s:
        if ss in l:
            b += 1
        
    if b == 0:
        print(i, end = ' ')
    
    else:
        print('-' * b, end = ' ')
   