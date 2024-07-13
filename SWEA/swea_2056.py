t = int(input())

for tt in range(t):
    date = input()

    d = int(date[6:8])

    if date[4:6] in ['01', '03', '05', '07', '08', '10', '12']:
        if d in range(1, 32):
            print(f'#{tt + 1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{tt + 1} -1')
    elif date[4:6] in ['04', '06', '09', '11']:
        if d in range(1, 31):
            print(f'#{tt + 1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{tt + 1} -1')
    elif date[4:6] in ['02']:
        if d in range(1, 29):
            print(f'#{tt + 1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{tt + 1} -1')
    else:
        print(f'#{tt + 1} -1')
