t = int(input())

for tt in range(t):
    n, k = map(int, input().split())
    xy = []
    for _ in range(n):
        x = list(map(int, input().split()))
        xy.append(x)
    r_l = []
    for i in range(n):
        c = 0
        
        for j in range(n):
            if xy[i][j] == 1:
                c += 1
            if xy[i][j] == 0 or j == n - 1:
                if c == k:
                    r_l.append(c)
                c = 0

        for j in range(n):
            if xy[j][i] == 1:
                c += 1
            if xy[j][i] == 0 or j == n - 1:
                if c == k:
                    r_l.append(c)
                c = 0

    
    
    print(f'#{tt + 1} {len(r_l)}')



# -----------------------

# t = int(input())

# for tt in range(t):
#     n, k = map(int, input().split())
#     xy = []
#     for _ in range(n):
#         x = list(map(int, input().split()))
#         xy.append(x)


#     r_l = []    
#     for row in xy:
#         c = 0
#         for r in range(n):
#             if row[r] == 0:
#                 if c == 0:
#                     c = 0
#                 elif c < k:
#                     c = 0
#                 elif c == k:
#                     c = k
#                 elif c > k:
#                     c = 0
#             if row[r] == 1:
#                 if c == k:
#                     if row[r - 1] == 0:
#                         c = k
#                     elif row[r - 1] == 1:
#                         c = k + 1
#                 else:
#                     c += 1
#         if c == 3:
#             r_l.append(c)
      
#     for col in range(n):
#         c2 = 0
#         temp = 0
#         for row2 in xy:
#             if row2[col] == 0:
#                 if c2 == 0:
#                     c2 = 0
#                 elif c2 < k:
#                     c2 = 0
#                 elif c2 == k:
#                     c2 = k
#                 elif c2 > k:
#                     c2 = 0
#                 temp = 0
#             if row2[col] == 1:
#                 if c2 != k:
#                     c2 += 1
#                 elif c2 == k:
#                     if temp == 0:
#                         c2 = k
#                     elif temp == 1:
#                         c2 = k + 1
#                 temp = 1
                
    
#         if c2 == k:
#             r_l.append(c2)
    
#     print(f'#{tt + 1} {len(r_l)}')





    


