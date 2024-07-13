for t in range(1, 11):
    n = int(input())
    board = []
    for _ in range(8):
        l = list(input())
        board.append(l)
    
    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            temp_x = board[i][j:j + n]
            re_temp_x = temp_x[::-1]
            if temp_x == re_temp_x:
                count += 1

    for i in range(8 - n + 1):
        for j in range(8):
            temp_y = []
            for k in range(i, i + n):
                temp_y.append(board[k][j])
            re_temp_y = temp_y[::-1]
            if temp_y == re_temp_y:
                count += 1

    print(f'#{t} {count}')
