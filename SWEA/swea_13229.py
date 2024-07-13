day = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}

t = int(input())

for tt in range(t):
    d = input()
    temp = day[d]
    print(f'#{tt + 1} {7 - temp}')