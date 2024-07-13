for tt in range(1, 11):
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    
    result = 0
    for i in range(n):
        temp = []
        for j in range(100):
            temp.append(table[j][i])

        while 1:
            if temp[0] == 0:
                del temp[0]
            elif temp[0] == 2:
                del temp[0]
            elif temp[0] == 1:
                break
            elif len(temp) == 0:
                break
        
        while 1:
            if temp[0] == 0:
                del temp[0]
            elif temp[0] == 1:
                del temp[0]
            elif temp[0] == 2:
                break
            elif len(temp) == 0:
                break

        c = 0
        for z in temp:
            if z == 1:
                if c == 0:
                    c += 1
            elif z == 2:
                if c == 1:
                    result += 1
                    c -= 1

        print(f'#{tt} {result}')

        

            



