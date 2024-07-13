t = int(input())

for tt in range(t):
    money = int(input())

    #50000
    a_50000 = money // 50000
    a_money = money % 50000

    b_10000 = a_money // 10000
    b_money = a_money % 10000

    c_5000 = b_money // 5000
    c_money = b_money % 5000

    d_1000 = c_money // 1000
    d_money = c_money % 1000

    e_500 = d_money // 500
    e_money = d_money % 500

    f_100 = e_money // 100
    f_money = e_money % 100

    g_50 = f_money // 50
    g_money = f_money % 50

    h_10 = g_money // 10

    print(f'#{tt + 1}')
    print(a_50000, b_10000, c_5000, d_1000, e_500, f_100, g_50, h_10)